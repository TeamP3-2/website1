document.addEventListener("DOMContentLoaded", function() {
    let preferencesForm = document.getElementById("coursesContainer");
    let loginForm = document.getElementById("loginForm");
    let signupForm = document.getElementById("signupForm");
    let logoutBtn = document.getElementById("logoutBtn");
    const storedName = localStorage.getItem("username");

    let currentPath = window.location.pathname.split("/").pop();
    let navLinks = document.querySelectorAll(".nav-list a");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });

    let storedEmail = localStorage.getItem("userEmail");

    if (logoutBtn) {
        if (storedEmail) {
            logoutBtn.style.display = "inline-block";
        } else {
            logoutBtn.style.display = "none";
        }

        logoutBtn.addEventListener("click", function() {
            let confirmLogout = confirm("هل تريد تسجيل الخروج؟");
            if (confirmLogout) {
                window.location.href = "signin.html";
            }
        });
    }

    if (preferencesForm) {
        fetch("http://localhost:3000/api/course")
        .then(response => response.json())
        .then(courses => {
            let coursesHTML = "";
            
            courses.slice(0, 6).forEach(course => {
                coursesHTML += `
                    <div class="course-card">
                        <h3>${course.title}</h3>
                        <p>${course.description}</p>
                        <p><strong>المدة:</strong> ${course.duration}</p>
                        <p><strong>المدرب:</strong> ${course.instructor}</p>
                        <p><strong>السعر:</strong> ${course.price}</p>
                        <button class="enroll-btn">التسجيل</button>
                    </div>
                `;
            });

            coursesContainer.innerHTML = coursesHTML;
        })
        .catch(error => console.error("❌ Error fetching courses:", error));
    }

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            event.preventDefault();
            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;

            let storedEmail = localStorage.getItem("userEmail");
            let storedPassword = localStorage.getItem("userPassword");

            if (email === storedEmail && password === storedPassword) {
                alert("🎉 مرحبًا بك مجددًا!");
                window.location.href = "index.html";
            } else {
                alert("❌ البريد الإلكتروني أو كلمة المرور غير صحيحة!");
            }
        });
    }

    if (signupForm) {
        signupForm.addEventListener("submit", function(event) {
            event.preventDefault();
            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;
            let name = document.getElementById("username").value;

            if (localStorage.getItem("userEmail") === email) {
                alert("❌ هذا البريد الإلكتروني مسجل بالفعل. حاول تسجيل الدخول.");
                return;
            }

            localStorage.setItem("userEmail", email);
            localStorage.setItem("userPassword", password);
            localStorage.setItem("username", name);

            alert("✅ تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.");
            window.location.href = "signin.html";
        });
    }
});
