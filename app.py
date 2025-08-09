from flask import Flask, render_template, request

app = Flask(__name__)

# قائمة طرق الدراسة مع خصائص كل طريقة
# يمكنك إضافة المزيد من الطرق والخصائص هنا
study_methods = [
    {
        "name": "طريقة بومودورو (Pomodoro)",
        "description": "تعتمد على تقسيم وقت المذاكرة إلى فترات قصيرة (25 دقيقة) مع استراحات قصيرة (5 دقائق).",
        "keywords": ["تركيز", "فترات قصيرة", "استراحات", "تشتت"]
    },
    {
        "name": "الخرائط الذهنية (Mind Maps)",
        "description": "استخدام الخرائط المرئية لربط المفاهيم والأفكار ببعضها البعض.",
        "keywords": ["بصري", "منظم", "إبداعي", "روابط"]
    },
    {
        "name": "طريقة استرجاع المعلومات النشط (Active Recall)",
        "description": "محاولة استرجاع المعلومات من الذاكرة دون النظر إلى المصدر.",
        "keywords": ["تذكر", "ممارسة", "تكرار", "فعال"]
    },
    {
        "name": "طريقة فاينمان (Feynman Technique)",
        "description": "شرح مفهوم معقد لشخص آخر ببساطة لضمان فهمك العميق له.",
        "keywords": ["شرح", "فهم عميق", "تبسيط", "تفكير"]
    },
    {
        "name": "طريقة SQ3R",
        "description": "تتكون من 5 خطوات: الاستطلاع، السؤال، القراءة، التسميع، المراجعة.",
        "keywords": ["قراءة", "تنظيم", "مراجعة", "تسميع"]
    },
    # ... أضف 25 طريقة أخرى بنفس الشكل هنا
]

@app.route('/')
def home():
    # قائمة بالأسئلة التي سيتم طرحها على المستخدم
    questions = [
        {"id": "q1", "text": "هل تفضل الدراسة لفترات طويلة أم قصيرة؟", "options": ["طويلة", "قصيرة"]},
        {"id": "q2", "text": "هل تفضل استخدام الأساليب البصرية أم الكتابية؟", "options": ["بصرية", "كتابية"]},
        {"id": "q3", "text": "هل تعاني من التشتت أثناء المذاكرة؟", "options": ["نعم", "لا"]},
    ]
    return render_template('index.html', questions=questions)

@app.route('/results', methods=['POST'])
def results():
    user_answers = request.form
    
    # قائمة لنتائج الفلترة
    filtered_methods = []
    
    # منطق الفلترة بناءً على إجابات المستخدم
    for method in study_methods:
        score = 0
        
        if "قصيرة" in user_answers.get('q1') and "فترات قصيرة" in method["keywords"]:
            score += 1
        if "بصرية" in user_answers.get('q2') and "بصري" in method["keywords"]:
            score += 1
        if "نعم" in user_answers.get('q3') and "تشتت" in method["keywords"]:
            score += 1

        if score > 0:
            filtered_methods.append((method, score))

    filtered_methods.sort(key=lambda x: x[1], reverse=True)
    top_methods = [item[0] for item in filtered_methods[:3]]
    
    return render_template('results.html', methods=top_methods)

if __name__ == '__main__':
    app.run(debug=True)
