/**
 * KTMT Quiz Master - Main Application Logic
 * Supports:
 * - Mode 1: Practice by individual exam (5 exams, 92 questions)
 * - Mode 2: Combined practice of all exams (configurable question count & categories)
 * - Customization: Shuffle (all, questions only, default), Mode (Study/Instant vs Exam/Timed)
 * - Mistakes review, Bookmarks, History, Keyboard shortcuts, Dark mode
 */

class QuizApp {
  constructor() {
    this.exams = typeof QUIZ_EXAMS !== 'undefined' ? QUIZ_EXAMS : [];
    this.currentExam = null;
    this.currentIndex = 0;
    this.userAnswers = {}; // index -> optionIndex
    this.flagged = new Set();
    this.timerInterval = null;
    this.timeRemaining = 0;
    this.timeTotal = 0;
    this.isSubmitted = false;
    this.isReviewMode = false;

    // Combined setup state
    this.combinedCount = 20;
    this.combinedShuffle = 'all';
    this.combinedMode = 'study';
    this.combinedSelectedCategories = new Set();

    // Modal exam setup state
    this.modalExamId = null;
    this.modalShuffle = 'all';
    this.modalMode = 'study';
    this.modalTimer = 'auto';

    // LocalStorage keys
    this.STORAGE_BOOKMARKS = 'ktmt_quiz_bookmarks';
    this.STORAGE_MISTAKES = 'ktmt_quiz_mistakes';
    this.STORAGE_HISTORY = 'ktmt_quiz_history';
    this.STORAGE_THEME = 'ktmt_quiz_theme';

    this.init();
  }

  init() {
    this.loadTheme();
    this.renderExamsGrid();
    this.initCombinedCategories();
    this.updateCounters();
    this.initKeyboardShortcuts();
  }

  /* ==================== THEME MANAGEMENT ==================== */
  loadTheme() {
    const savedTheme = localStorage.getItem(this.STORAGE_THEME) || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) btn.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
  }

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const newTheme = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem(this.STORAGE_THEME, newTheme);
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) btn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
  }

  /* ==================== LOCAL STORAGE HELPERS ==================== */
  getBookmarks() {
    try {
      return JSON.parse(localStorage.getItem(this.STORAGE_BOOKMARKS)) || [];
    } catch {
      return [];
    }
  }

  saveBookmarks(list) {
    localStorage.setItem(this.STORAGE_BOOKMARKS, JSON.stringify(list));
    this.updateCounters();
  }

  isBookmarked(qId) {
    return this.getBookmarks().includes(qId);
  }

  toggleBookmark(qId) {
    let list = this.getBookmarks();
    if (list.includes(qId)) {
      list = list.filter(id => id !== qId);
    } else {
      list.push(qId);
    }
    this.saveBookmarks(list);
    return list.includes(qId);
  }

  getMistakes() {
    try {
      return JSON.parse(localStorage.getItem(this.STORAGE_MISTAKES)) || [];
    } catch {
      return [];
    }
  }

  recordMistake(q) {
    let mistakes = this.getMistakes();
    const existing = mistakes.find(m => m.id === q.id);
    if (existing) {
      existing.count = (existing.count || 1) + 1;
      existing.lastTime = Date.now();
    } else {
      mistakes.push({
        id: q.id,
        content: q.content,
        category: q.category,
        exam_id: q.exam_id,
        count: 1,
        lastTime: Date.now()
      });
    }
    localStorage.setItem(this.STORAGE_MISTAKES, JSON.stringify(mistakes));
    this.updateCounters();
  }

  removeMistake(qId) {
    let mistakes = this.getMistakes().filter(m => m.id !== qId);
    localStorage.setItem(this.STORAGE_MISTAKES, JSON.stringify(mistakes));
    this.updateCounters();
  }

  getHistory() {
    try {
      return JSON.parse(localStorage.getItem(this.STORAGE_HISTORY)) || [];
    } catch {
      return [];
    }
  }

  recordHistory(record) {
    let history = this.getHistory();
    history.unshift(record);
    if (history.length > 50) history = history.slice(0, 50);
    localStorage.setItem(this.STORAGE_HISTORY, JSON.stringify(history));
  }

  updateCounters() {
    const bCount = this.getBookmarks().length;
    const mCount = this.getMistakes().length;

    const hB = document.getElementById('header-bookmark-count');
    const hM = document.getElementById('header-mistakes-count');
    const tB = document.getElementById('tab-bookmarks-badge');
    const tM = document.getElementById('tab-mistakes-badge');

    if (hB) hB.textContent = bCount;
    if (hM) hM.textContent = mCount;
    if (tB) tB.textContent = `(${bCount})`;
    if (tM) tM.textContent = `(${mCount})`;
  }

  /* ==================== DASHBOARD & TABS ==================== */
  switchTab(tabId) {
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
    });

    const panes = ['by-exam', 'combined', 'mistakes', 'bookmarks', 'history'];
    panes.forEach(p => {
      const el = document.getElementById(`tab-${p}-content`);
      if (el) el.style.display = p === tabId ? 'block' : 'none';
    });

    if (tabId === 'mistakes') this.renderMistakesTab();
    if (tabId === 'bookmarks') this.renderBookmarksTab();
    if (tabId === 'history') this.renderHistoryTab();
  }

  showDashboard() {
    clearInterval(this.timerInterval);
    document.getElementById('dashboard-view').style.display = 'block';
    document.getElementById('exam-view').classList.remove('active');
    this.updateCounters();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /* ==================== MỤC 1: ÔN THEO ĐỀ ==================== */
  renderExamsGrid() {
    const container = document.getElementById('exams-container');
    if (!container) return;
    container.innerHTML = '';

    const history = this.getHistory();

    this.exams.forEach(exam => {
      // Find highest score for this exam
      const attempts = history.filter(h => h.examId === exam.id);
      let bestScoreText = 'Chưa thi';
      if (attempts.length > 0) {
        const best = Math.max(...attempts.map(a => a.score10));
        bestScoreText = `Điểm cao nhất: ${best.toFixed(1)}/10`;
      }

      const card = document.createElement('div');
      card.className = 'exam-card';
      card.innerHTML = `
        <div>
          <div class="exam-card-header">
            <span class="exam-badge">Đề số ${exam.id}</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">${bestScoreText}</span>
          </div>
          <h3 class="exam-card-title">${exam.title}</h3>
          <p class="exam-card-desc">${exam.description}</p>
        </div>
        <div>
          <div class="exam-meta">
            <div class="exam-meta-item"><span>📝</span> ${exam.questions.length} câu hỏi</div>
            <div class="exam-meta-item"><span>⏱️</span> ${exam.duration_minutes} phút</div>
            <div class="exam-meta-item"><span>🎯</span> Trắc nghiệm 4 lựa chọn</div>
          </div>
          <div class="exam-card-actions">
            <button class="btn-primary" onclick="app.quickStartExam(${exam.id})">
              🚀 Làm bài ngay
            </button>
            <button class="btn-secondary" title="Tùy chỉnh xáo trộn, chế độ ôn" onclick="app.openExamConfigModal(${exam.id})">
              ⚙️ Tùy chọn
            </button>
          </div>
        </div>
      `;
      container.appendChild(card);
    });
  }

  quickStartExam(examId) {
    this.startExamSession({
      examId: examId,
      shuffleType: 'all', // Default: shuffle all
      mode: 'study', // Default: Study mode with instant feedback
      durationMinutes: null // Auto
    });
  }

  openExamConfigModal(examId) {
    const exam = this.exams.find(e => e.id === examId);
    if (!exam) return;
    this.modalExamId = examId;
    document.getElementById('modal-exam-title').textContent = `⚙️ Tùy chọn: ${exam.title}`;

    // Reset selection in modal
    this.selectModalShuffle('all');
    this.selectModalMode('study');
    this.selectModalTimer('auto');

    this.openModal('exam-config-modal');
  }

  selectModalShuffle(type) {
    this.modalShuffle = type;
    document.querySelectorAll('[data-modal-shuffle]').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-modal-shuffle') === type);
    });
  }

  selectModalMode(mode) {
    this.modalMode = mode;
    document.querySelectorAll('[data-modal-mode]').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-modal-mode') === mode);
    });
    const timerGroup = document.getElementById('modal-timer-group');
    if (timerGroup) {
      timerGroup.style.display = mode === 'exam' ? 'block' : 'none';
    }
  }

  selectModalTimer(val) {
    this.modalTimer = val;
    document.querySelectorAll('#modal-timer-chips .chip-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-time') === String(val));
    });
  }

  startConfiguredExam() {
    this.closeModal('exam-config-modal');
    const exam = this.exams.find(e => e.id === this.modalExamId);
    if (!exam) return;

    let duration = null;
    if (this.modalMode === 'exam') {
      if (this.modalTimer === 'auto') duration = exam.duration_minutes;
      else duration = parseInt(this.modalTimer, 10);
    }

    this.startExamSession({
      examId: this.modalExamId,
      shuffleType: this.modalShuffle,
      mode: this.modalMode,
      durationMinutes: duration
    });
  }

  /* ==================== MỤC 2: ÔN TỔNG HỢP ==================== */
  initCombinedCategories() {
    const container = document.getElementById('combined-categories-container');
    if (!container) return;

    // Collect unique categories across all exams
    const cats = new Set();
    this.exams.forEach(e => {
      e.questions.forEach(q => {
        if (q.category) cats.add(q.category);
      });
    });

    container.innerHTML = '';
    cats.forEach(cat => {
      const label = document.createElement('label');
      label.className = 'tag-checkbox';
      label.innerHTML = `
        <input type="checkbox" value="${cat}" checked onchange="app.toggleCategoryFilter('${cat}')">
        <span>${cat}</span>
      `;
      container.appendChild(label);
      this.combinedSelectedCategories.add(cat);
    });
  }

  toggleCategoryFilter(cat) {
    if (this.combinedSelectedCategories.has(cat)) {
      this.combinedSelectedCategories.delete(cat);
    } else {
      this.combinedSelectedCategories.add(cat);
    }
  }

  selectCombinedCount(count) {
    this.combinedCount = count;
    document.querySelectorAll('#combined-count-chips .chip-btn').forEach(btn => {
      btn.classList.toggle('active', parseInt(btn.getAttribute('data-count'), 10) === count);
    });
  }

  selectCombinedShuffle(type) {
    this.combinedShuffle = type;
    document.querySelectorAll('#tab-combined-content [data-shuffle]').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-shuffle') === type);
    });
  }

  selectCombinedMode(mode) {
    this.combinedMode = mode;
    document.querySelectorAll('#tab-combined-content [data-mode]').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-mode') === mode);
    });
  }

  startCombinedExam() {
    // Collect all pool questions
    let pool = [];
    this.exams.forEach(exam => {
      exam.questions.forEach(q => {
        if (this.combinedSelectedCategories.size === 0 || this.combinedSelectedCategories.has(q.category)) {
          pool.push({ ...q, origin_exam_title: exam.title });
        }
      });
    });

    if (pool.length === 0) {
      alert('Vui lòng chọn ít nhất 1 chuyên đề kiến thức!');
      return;
    }

    // Determine target count
    const targetCount = Math.min(this.combinedCount, pool.length);

    // Shuffle pool if requested
    if (this.combinedShuffle !== 'default') {
      pool = this.shuffleArray([...pool]);
    }
    const selectedQuestions = pool.slice(0, targetCount);

    this.startExamSession({
      customTitle: `Ôn tổng hợp: ${targetCount} câu hỏi (${this.combinedMode === 'study' ? 'Luyện tập' : 'Thi thử'})`,
      customQuestions: selectedQuestions,
      shuffleType: this.combinedShuffle,
      mode: this.combinedMode,
      durationMinutes: this.combinedMode === 'exam' ? Math.round(targetCount * 1.5) : null
    });
  }

  /* ==================== EXAM SESSION LOGIC ==================== */
  startExamSession(config) {
    let rawQuestions = [];
    let title = '';

    if (config.examId) {
      const exam = this.exams.find(e => e.id === config.examId);
      if (!exam) return;
      title = exam.title;
      rawQuestions = exam.questions.map(q => ({ ...q, origin_exam_title: exam.title }));
    } else if (config.customQuestions) {
      title = config.customTitle || 'Bài làm tổng hợp';
      rawQuestions = config.customQuestions;
    }

    if (rawQuestions.length === 0) {
      alert('Không có câu hỏi nào để bắt đầu!');
      return;
    }

    // Process questions and options based on shuffleType
    let preparedQuestions = rawQuestions.map(q => {
      const cloned = { ...q, options: [...q.options] };
      // Shuffle options if shuffleType === 'all'
      if (config.shuffleType === 'all') {
        const correctText = cloned.options[cloned.correct_index];
        const shuffledOptions = this.shuffleArray([...cloned.options]);
        cloned.options = shuffledOptions;
        cloned.correct_index = shuffledOptions.indexOf(correctText);
      }
      return cloned;
    });

    // Shuffle question order if shuffleType is 'all' or 'questions'
    if (config.shuffleType === 'all' || config.shuffleType === 'questions') {
      preparedQuestions = this.shuffleArray(preparedQuestions);
    }

    // Setup active exam state
    this.currentExam = {
      id: config.examId || 'custom',
      title: title,
      mode: config.mode,
      shuffleType: config.shuffleType,
      questions: preparedQuestions,
      durationMinutes: config.durationMinutes
    };

    this.currentIndex = 0;
    this.userAnswers = {};
    this.flagged.clear();
    this.isSubmitted = false;
    this.isReviewMode = false;

    // Timer setup
    clearInterval(this.timerInterval);
    const timerPill = document.getElementById('exam-timer-pill');
    if (config.mode === 'exam' && config.durationMinutes && config.durationMinutes > 0) {
      this.timeRemaining = config.durationMinutes * 60;
      this.timeTotal = this.timeRemaining;
      timerPill.style.display = 'flex';
      this.updateTimerDisplay();
      this.startTimer();
    } else {
      timerPill.style.display = 'none';
      this.timeRemaining = 0;
      this.timeTotal = 0;
    }

    // Switch view
    document.getElementById('dashboard-view').style.display = 'none';
    document.getElementById('exam-view').classList.add('active');
    document.getElementById('exam-title-display').textContent = title;

    // Render palette and first question
    this.renderPalette();
    this.renderCurrentQuestion();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  startTimer() {
    this.timerInterval = setInterval(() => {
      this.timeRemaining--;
      this.updateTimerDisplay();
      if (this.timeRemaining <= 0) {
        clearInterval(this.timerInterval);
        alert('⏰ Hết giờ làm bài! Hệ thống đang tự động nộp bài...');
        this.submitExam();
      }
    }, 1000);
  }

  updateTimerDisplay() {
    const min = Math.floor(this.timeRemaining / 60);
    const sec = this.timeRemaining % 60;
    const str = `${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
    const display = document.getElementById('timer-display');
    if (display) display.textContent = str;

    const pill = document.getElementById('exam-timer-pill');
    if (pill) {
      pill.classList.toggle('urgent', this.timeRemaining < 180); // Urgent when < 3 mins
    }
  }

  /* ==================== QUESTION RENDERING & INTERACTION ==================== */
  renderCurrentQuestion() {
    if (!this.currentExam) return;
    const q = this.currentExam.questions[this.currentIndex];
    const total = this.currentExam.questions.length;

    // Update badges
    document.getElementById('q-index-badge').textContent = `Câu ${this.currentIndex + 1} / ${total}`;
    document.getElementById('q-category-badge').textContent = q.category || 'KTMT';
    document.getElementById('q-origin-badge').textContent = q.origin_exam_title || `Đề số ${q.exam_id || 1}`;

    // Flag button state
    const flagBtn = document.getElementById('q-flag-btn');
    const isFlagged = this.flagged.has(this.currentIndex);
    flagBtn.classList.toggle('flagged', isFlagged);
    document.getElementById('q-flag-text').textContent = isFlagged ? 'Đã đánh dấu' : 'Đánh dấu';

    // Content
    document.getElementById('q-content-display').textContent = q.content;

    // Code block
    const codeContainer = document.getElementById('q-code-container');
    const codeDisplay = document.getElementById('q-code-display');
    if (q.code && q.code.trim()) {
      codeContainer.style.display = 'block';
      codeDisplay.textContent = q.code;
    } else {
      codeContainer.style.display = 'none';
    }

    // Options
    const optContainer = document.getElementById('q-options-container');
    optContainer.innerHTML = '';

    const letters = ['A', 'B', 'C', 'D'];
    const userAnswer = this.userAnswers[this.currentIndex];
    const isAnswered = userAnswer !== undefined;
    const isStudy = this.currentExam.mode === 'study';

    q.options.forEach((opt, idx) => {
      const item = document.createElement('div');
      item.className = 'option-item';

      if (userAnswer === idx) {
        item.classList.add('selected');
      }

      // In Study mode or Review mode, highlight correctness
      if ((isStudy && isAnswered) || this.isReviewMode) {
        if (idx === q.correct_index) {
          item.classList.add('correct');
        } else if (userAnswer === idx) {
          item.classList.add('incorrect');
        }
      }

      item.innerHTML = `
        <div class="option-key">${letters[idx]}</div>
        <div class="option-text">${opt}</div>
      `;

      item.onclick = () => this.handleSelectOption(idx);
      optContainer.appendChild(item);
    });

    // Explanation Box
    const expBox = document.getElementById('q-explanation-box');
    const expText = document.getElementById('q-explanation-text');
    if ((isStudy && isAnswered) || this.isReviewMode) {
      expBox.classList.add('active');
      expText.textContent = q.explanation || 'Không có giải thích chi tiết.';
    } else {
      expBox.classList.remove('active');
    }

    // Navigation buttons
    document.getElementById('btn-prev-question').disabled = this.currentIndex === 0;
    const btnNext = document.getElementById('btn-next-question');
    if (this.currentIndex === total - 1) {
      btnNext.textContent = 'Hoàn thành ✓';
    } else {
      btnNext.textContent = 'Câu sau →';
    }

    // Progress bar update
    const answeredCount = Object.keys(this.userAnswers).length;
    const pct = Math.round((answeredCount / total) * 100);
    document.getElementById('progress-text').textContent = `Đã làm ${answeredCount}/${total} câu (${pct}%)`;
    document.getElementById('progress-bar-fill').style.width = `${pct}%`;

    // Highlight palette button
    this.updatePaletteActive();
  }

  handleSelectOption(optionIndex) {
    if (this.isReviewMode) return; // Read-only in review mode

    const q = this.currentExam.questions[this.currentIndex];
    const isStudy = this.currentExam.mode === 'study';

    this.userAnswers[this.currentIndex] = optionIndex;

    // If in study mode, record mistake if incorrect
    if (isStudy) {
      if (optionIndex !== q.correct_index) {
        this.recordMistake(q);
      } else {
        // Answered correctly, could remove from mistakes
      }
    }

    this.renderCurrentQuestion();
    this.renderPalette();
  }

  toggleCurrentFlag() {
    if (this.flagged.has(this.currentIndex)) {
      this.flagged.delete(this.currentIndex);
    } else {
      this.flagged.add(this.currentIndex);
    }

    // Also toggle persistent bookmark
    const q = this.currentExam.questions[this.currentIndex];
    if (q && q.id) {
      this.toggleBookmark(q.id);
    }

    this.renderCurrentQuestion();
    this.renderPalette();
  }

  goToQuestion(idx) {
    if (!this.currentExam || idx < 0 || idx >= this.currentExam.questions.length) return;
    this.currentIndex = idx;
    this.renderCurrentQuestion();
  }

  goToPrevQuestion() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.renderCurrentQuestion();
    }
  }

  goToNextQuestion() {
    if (!this.currentExam) return;
    if (this.currentIndex < this.currentExam.questions.length - 1) {
      this.currentIndex++;
      this.renderCurrentQuestion();
    } else {
      this.confirmSubmitExam();
    }
  }

  /* ==================== PALETTE SIDEBAR ==================== */
  renderPalette() {
    if (!this.currentExam) return;
    const container = document.getElementById('palette-grid-container');
    if (!container) return;
    container.innerHTML = '';

    const questions = this.currentExam.questions;
    const isStudy = this.currentExam.mode === 'study';

    questions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = idx + 1;

      if (idx === this.currentIndex) {
        btn.classList.add('current');
      }

      const isAnswered = this.userAnswers[idx] !== undefined;
      if (isAnswered) {
        btn.classList.add('answered');

        if ((isStudy && isAnswered) || this.isReviewMode) {
          const isCorrect = this.userAnswers[idx] === q.correct_index;
          btn.classList.add(isCorrect ? 'correct' : 'incorrect');
        }
      }

      if (this.flagged.has(idx)) {
        btn.classList.add('flagged');
      }

      btn.onclick = () => this.goToQuestion(idx);
      container.appendChild(btn);
    });

    const answeredCount = Object.keys(this.userAnswers).length;
    document.getElementById('palette-count-summary').textContent = `${answeredCount}/${questions.length} đã làm`;
  }

  updatePaletteActive() {
    document.querySelectorAll('.palette-btn').forEach((btn, idx) => {
      btn.classList.toggle('current', idx === this.currentIndex);
    });
  }

  /* ==================== EXAM SUBMISSION & RESULTS ==================== */
  confirmSubmitExam() {
    const total = this.currentExam.questions.length;
    const answeredCount = Object.keys(this.userAnswers).length;
    const unanswered = total - answeredCount;

    let msg = `Bạn đã hoàn thành ${answeredCount}/${total} câu hỏi.`;
    if (unanswered > 0) {
      msg += `\n⚠️ Vẫn còn ${unanswered} câu chưa làm! Bạn có chắc chắn muốn nộp bài không?`;
    } else {
      msg += `\nBạn có muốn nộp bài để xem kết quả không?`;
    }

    if (confirm(msg)) {
      this.submitExam();
    }
  }

  submitExam() {
    clearInterval(this.timerInterval);
    this.isSubmitted = true;

    const questions = this.currentExam.questions;
    const total = questions.length;
    let correctCount = 0;
    const categoryStats = {};

    questions.forEach((q, idx) => {
      const cat = q.category || 'Khác';
      if (!categoryStats[cat]) {
        categoryStats[cat] = { total: 0, correct: 0 };
      }
      categoryStats[cat].total++;

      const userAns = this.userAnswers[idx];
      if (userAns !== undefined && userAns === q.correct_index) {
        correctCount++;
        categoryStats[cat].correct++;
      } else {
        // Record mistake for review
        this.recordMistake(q);
      }
    });

    // Score on 10-point scale
    const score10 = Math.round((correctCount / total) * 100) / 10;
    const accuracyPct = Math.round((correctCount / total) * 100);

    // Calculate time taken
    let timeTakenStr = 'Không tính giờ';
    if (this.timeTotal > 0) {
      const elapsed = this.timeTotal - this.timeRemaining;
      const m = Math.floor(elapsed / 60);
      const s = elapsed % 60;
      timeTakenStr = `${m} phút ${s} giây`;
    }

    // Save history
    this.recordHistory({
      examId: this.currentExam.id,
      title: this.currentExam.title,
      date: new Date().toLocaleString('vi-VN'),
      correctCount: correctCount,
      totalCount: total,
      score10: score10,
      accuracyPct: accuracyPct,
      timeTaken: timeTakenStr,
      mode: this.currentExam.mode
    });

    // Update result modal DOM
    document.getElementById('result-score-10').textContent = score10.toFixed(1);
    document.getElementById('result-correct-count').textContent = `${correctCount}/${total}`;
    document.getElementById('result-accuracy-pct').textContent = `${accuracyPct}%`;
    document.getElementById('result-time-taken').textContent = timeTakenStr;

    // Badge styling & message
    const badge = document.getElementById('result-badge-text');
    badge.className = 'result-badge';
    if (score10 >= 8.5) {
      badge.classList.add('excellent');
      badge.textContent = '🏆 Xuất sắc! Bạn nắm rất vững kiến thức KTMT';
    } else if (score10 >= 7.0) {
      badge.classList.add('good');
      badge.textContent = '🎉 Giỏi! Kết quả rất tốt, sẵn sàng cho kỳ thi';
    } else if (score10 >= 5.0) {
      badge.classList.add('average');
      badge.textContent = '👍 Đạt yêu cầu! Nên ôn lại các câu đã làm sai';
    } else {
      badge.classList.add('need-study');
      badge.textContent = '⚠️ Cần ôn tập thêm! Hãy xem lại kỹ lời giải các câu sai';
    }

    // Category breakdown DOM
    const catContainer = document.getElementById('result-category-breakdown');
    catContainer.innerHTML = '<h4>Phân tích theo chuyên đề:</h4>';
    Object.keys(categoryStats).forEach(cat => {
      const item = categoryStats[cat];
      const pct = Math.round((item.correct / item.total) * 100);
      const row = document.createElement('div');
      row.className = 'breakdown-item';
      row.innerHTML = `
        <div class="breakdown-header">
          <span>${cat}</span>
          <span style="font-weight: 600;">${item.correct}/${item.total} (${pct}%)</span>
        </div>
        <div class="breakdown-bar-bg">
          <div class="breakdown-bar-fill" style="width: ${pct}%; background: ${pct >= 70 ? 'var(--success)' : (pct >= 40 ? 'var(--warning)' : 'var(--danger)')};"></div>
        </div>
      `;
      catContainer.appendChild(row);
    });

    this.openModal('result-modal');
  }

  reviewExamAnswers() {
    this.closeModal('result-modal');
    this.isReviewMode = true;
    this.currentIndex = 0;
    this.renderCurrentQuestion();
    this.renderPalette();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  retryCurrentExam() {
    this.closeModal('result-modal');
    this.startExamSession({
      examId: this.currentExam.id === 'custom' ? null : this.currentExam.id,
      customTitle: this.currentExam.title,
      customQuestions: this.currentExam.id === 'custom' ? this.currentExam.questions : null,
      shuffleType: this.currentExam.shuffleType,
      mode: this.currentExam.mode,
      durationMinutes: this.currentExam.durationMinutes
    });
  }

  confirmExitExam() {
    if (this.isSubmitted || this.isReviewMode) {
      this.showDashboard();
      return;
    }
    if (confirm('Bạn có chắc muốn thoát bài thi hiện tại không? Tiến trình làm bài sẽ không được lưu.')) {
      this.showDashboard();
    }
  }

  /* ==================== MISTAKES & BOOKMARKS TABS ==================== */
  renderMistakesTab() {
    const container = document.getElementById('mistakes-list-container');
    if (!container) return;
    const mistakes = this.getMistakes();

    if (mistakes.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon">🎉</div>
          <h3>Chưa có câu sai nào!</h3>
          <p>Tuyệt vời! Bạn chưa làm sai câu hỏi nào hoặc đã ôn sạch các câu sai.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-weight: 600; color: var(--danger);">Tổng số: ${mistakes.length} câu làm sai</span>
        <button class="btn-primary" onclick="app.practiceMistakes()">
          🚀 Luyện tập toàn bộ ${mistakes.length} câu sai này
        </button>
      </div>
    `;

    mistakes.forEach((m, idx) => {
      const card = document.createElement('div');
      card.className = 'exam-card';
      card.style.marginBottom = '0.75rem';
      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
          <span class="exam-badge" style="background: var(--danger-light); color: var(--danger);">Sai ${m.count || 1} lần</span>
          <button class="btn-secondary" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;" onclick="app.removeMistake('${m.id}')">Đã thuộc (Xóa)</button>
        </div>
        <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">${m.content}</div>
        <div style="font-size: 0.75rem; color: var(--text-muted);">Chuyên đề: ${m.category}</div>
      `;
      container.appendChild(card);
    });
  }

  practiceMistakes() {
    const mistakes = this.getMistakes();
    if (mistakes.length === 0) return;

    // Find full question objects
    const mistakeIds = new Set(mistakes.map(m => m.id));
    const fullQuestions = [];
    this.exams.forEach(e => {
      e.questions.forEach(q => {
        if (mistakeIds.has(q.id)) {
          fullQuestions.push({ ...q, origin_exam_title: e.title });
        }
      });
    });

    if (fullQuestions.length === 0) {
      alert('Không tìm thấy dữ liệu câu hỏi!');
      return;
    }

    this.startExamSession({
      customTitle: `Luyện tập ${fullQuestions.length} câu đã làm sai`,
      customQuestions: fullQuestions,
      shuffleType: 'all',
      mode: 'study', // Study mode for learning
      durationMinutes: null
    });
  }

  clearMistakes() {
    if (confirm('Bạn có chắc muốn xóa toàn bộ danh sách câu làm sai không?')) {
      localStorage.removeItem(this.STORAGE_MISTAKES);
      this.updateCounters();
      this.renderMistakesTab();
    }
  }

  renderBookmarksTab() {
    const container = document.getElementById('bookmarks-list-container');
    if (!container) return;
    const bookmarkIds = this.getBookmarks();

    if (bookmarkIds.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon">⭐</div>
          <h3>Chưa có câu hỏi nào được đánh dấu</h3>
          <p>Khi làm bài thi, bấm nút "Đánh dấu" hoặc phím F để lưu các câu hỏi quan trọng vào đây.</p>
        </div>
      `;
      return;
    }

    // Find full questions
    const fullQuestions = [];
    this.exams.forEach(e => {
      e.questions.forEach(q => {
        if (bookmarkIds.includes(q.id)) {
          fullQuestions.push({ ...q, origin_exam_title: e.title });
        }
      });
    });

    container.innerHTML = `
      <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-weight: 600; color: var(--primary);">Đã đánh dấu: ${fullQuestions.length} câu</span>
        <button class="btn-primary" onclick="app.practiceBookmarks()">
          🚀 Luyện tập các câu đã đánh dấu
        </button>
      </div>
    `;

    fullQuestions.forEach((q, idx) => {
      const card = document.createElement('div');
      card.className = 'exam-card';
      card.style.marginBottom = '0.75rem';
      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
          <span class="exam-badge">${q.category}</span>
          <button class="btn-secondary" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;" onclick="app.toggleBookmark('${q.id}'); app.renderBookmarksTab();">Bỏ lưu ⭐</button>
        </div>
        <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 0.35rem;">${q.content}</div>
        <div style="font-size: 0.75rem; color: var(--text-muted);">${q.origin_exam_title || ''}</div>
      `;
      container.appendChild(card);
    });
  }

  practiceBookmarks() {
    const bookmarkIds = this.getBookmarks();
    const fullQuestions = [];
    this.exams.forEach(e => {
      e.questions.forEach(q => {
        if (bookmarkIds.includes(q.id)) {
          fullQuestions.push({ ...q, origin_exam_title: e.title });
        }
      });
    });

    if (fullQuestions.length === 0) return;

    this.startExamSession({
      customTitle: `Luyện tập ${fullQuestions.length} câu đã đánh dấu`,
      customQuestions: fullQuestions,
      shuffleType: 'all',
      mode: 'study',
      durationMinutes: null
    });
  }

  clearBookmarks() {
    if (confirm('Bạn có chắc muốn bỏ lưu toàn bộ câu hỏi đã đánh dấu không?')) {
      localStorage.removeItem(this.STORAGE_BOOKMARKS);
      this.updateCounters();
      this.renderBookmarksTab();
    }
  }

  renderHistoryTab() {
    const container = document.getElementById('history-list-container');
    if (!container) return;
    const history = this.getHistory();

    if (history.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon">📊</div>
          <h3>Chưa có lịch sử làm bài</h3>
          <p>Hãy hoàn thành một đề thi để theo dõi điểm số và tiến độ của bạn tại đây!</p>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        ${history.map(h => `
          <div class="exam-card" style="padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="exam-card-title" style="margin: 0; font-size: 1rem;">${h.title}</span>
              <span style="font-size: 1.15rem; font-weight: 800; color: ${h.score10 >= 7 ? 'var(--success)' : (h.score10 >= 5 ? 'var(--primary)' : 'var(--danger)')};">
                ${h.score10.toFixed(1)}/10
              </span>
            </div>
            <div style="display: flex; gap: 1.25rem; font-size: 0.8rem; color: var(--text-muted);">
              <span>📅 ${h.date}</span>
              <span>🎯 Đúng ${h.correctCount}/${h.totalCount} (${h.accuracyPct}%)</span>
              <span>⏱️ ${h.timeTaken}</span>
              <span>🏷️ ${h.mode === 'study' ? 'Luyện tập' : 'Thi thử'}</span>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  clearHistory() {
    if (confirm('Bạn có chắc muốn xóa toàn bộ lịch sử thi không?')) {
      localStorage.removeItem(this.STORAGE_HISTORY);
      this.renderHistoryTab();
      this.renderExamsGrid();
    }
  }

  /* ==================== MODAL HELPERS ==================== */
  openModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) m.classList.add('active');
  }

  closeModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) m.classList.remove('active');
  }

  openShortcutsModal() {
    this.openModal('shortcuts-modal');
  }

  /* ==================== KEYBOARD SHORTCUTS ==================== */
  initKeyboardShortcuts() {
    window.addEventListener('keydown', e => {
      // Ignore if user is typing in input or textarea
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;

      // Escape to close open modal
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
        return;
      }

      // Check if on exam view
      const examView = document.getElementById('exam-view');
      if (examView && examView.classList.contains('active')) {
        const key = e.key.toLowerCase();

        // 1, 2, 3, 4 or a, b, c, d
        if (['1', 'a'].includes(key)) {
          e.preventDefault();
          this.handleSelectOption(0);
        } else if (['2', 'b'].includes(key)) {
          e.preventDefault();
          this.handleSelectOption(1);
        } else if (['3', 'c'].includes(key)) {
          e.preventDefault();
          this.handleSelectOption(2);
        } else if (['4', 'd'].includes(key)) {
          e.preventDefault();
          this.handleSelectOption(3);
        } else if (['arrowleft', 'j'].includes(key)) {
          e.preventDefault();
          this.goToPrevQuestion();
        } else if (['arrowright', 'k'].includes(key)) {
          e.preventDefault();
          this.goToNextQuestion();
        } else if (key === 'f') {
          e.preventDefault();
          this.toggleCurrentFlag();
        }
      }

      // Global shortcuts
      if (e.key.toLowerCase() === 't') {
        this.toggleTheme();
      }
    });
  }
}

// Instantiate App
const app = new QuizApp();
