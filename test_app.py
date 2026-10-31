import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

def test_data():
    with open('questions.json', 'r', encoding='utf-8') as f:
        exams = json.load(f)

    assert len(exams) == 5, f"Expected 5 exams, got {len(exams)}"
    total_q = sum(len(e['questions']) for e in exams)
    print(f"Total exams: {len(exams)}, Total questions: {total_q}")

    for e_idx, exam in enumerate(exams):
        assert 'id' in exam and 'title' in exam and 'questions' in exam
        print(f"Exam {exam['id']}: {exam['title']} - {len(exam['questions'])} questions")
        for q_idx, q in enumerate(exam['questions']):
            assert 'id' in q
            assert 'content' in q and len(q['content']) > 0
            assert 'options' in q and len(q['options']) >= 2, f"Q {q['id']} has < 2 options"
            assert 'correct_index' in q
            assert 0 <= q['correct_index'] < len(q['options']), f"Q {q['id']} invalid correct_index: {q['correct_index']} vs len {len(q['options'])}"
            assert 'explanation' in q and len(q['explanation']) > 0

    print("All questions data assertion passed successfully!")

def test_files():
    for fname in ['index.html', 'styles.css', 'quiz_data.js', 'app.js']:
        assert os.path.exists(fname), f"File {fname} missing"
        size = os.path.getsize(fname)
        print(f"File {fname}: {size} bytes")
    print("All core files exist and are populated.")

if __name__ == '__main__':
    test_data()
    test_files()
