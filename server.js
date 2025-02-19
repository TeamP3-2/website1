const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));
// تحديد المسار الافتراضي لصفحة index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'html', 'landing.html'));
});

// بيانات الكورس
const courses = [
    {
        id: 1,
        title: "أساسيات البرمجة بلغة JavaScript",
        description: "تعلم أساسيات JavaScript من الصفر إلى الاحتراف.",
        duration: "4 أسابيع",
        instructor: "محمد خالد",
        price: "مجاني"
    },
    {
        id: 2,
        title: "مقدمة في الذكاء الاصطناعي",
        description: "اكتشف عالم الذكاء الاصطناعي وخوارزمياته الأساسية.",
        duration: "6 أسابيع",
        instructor: "د. أحمد علي",
        price: "مجاني"
    },
    {
        id: 3,
        title: "تطوير تطبيقات الويب باستخدام React",
        description: "دورة شاملة لبناء تطبيقات ويب تفاعلية باستخدام React.js.",
        duration: "5 أسابيع",
        instructor: "سارة حسن",
        price: "مجاني"
    },
    {
        id: 4,
        title: "تحليل البيانات باستخدام Python",
        description: "تعلم تحليل البيانات بلغة Python باستخدام Pandas و NumPy.",
        duration: "7 أسابيع",
        instructor: "ياسر محمود",
        price: "مجاني"
    },
    {
        id: 5,
        title: "أساسيات الأمن السيبراني",
        description: "تعرف على المفاهيم الأساسية لحماية المعلومات والأمان السيبراني.",
        duration: "3 أسابيع",
        instructor: "نورا سعيد",
        price: "مجاني"
    },
    {
        id: 6,
        title: "أساسيات الأمن السيبراني",
        description: "تعرف على المفاهيم الأساسية لحماية المعلومات والأمان السيبراني.",
        duration: "3 أسابيع",
        instructor: "نورا سعيد",
        price: "مجاني"
    }
];
app.get('/api/course', (req, res) => {
    res.json(courses); // إرجاع بيانات الكورس على شكل JSON
});

app.get('/:page', (req, res) => {
    const pagePath = path.join(__dirname, 'public', 'html', req.params.page);
    res.sendFile(pagePath, (err) => {
        if (err) {
            res.status(404).send("الصفحة غير موجودة!");
        }
    });
});
// API Endpoint لجلب معلومات الكورس

app.listen(port, () => {
    console.log(`API is running on http://localhost:${port}`);
});
