def add_all(*args):
    return sum(args)

def make_student(**kwargs):
    return kwargs

def send_score(student_id, *, subject, score):
    print(f"學號 {student_id}｜{subject}：{score} 分")

def report(title, *scores, prefix="成績"):
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")
