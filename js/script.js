
document.addEventListener("DOMContentLoaded", function() {
    let preferencesForm = document.getElementById("preferencesForm");
    let loginForm = document.getElementById("loginForm");
    let signupForm = document.getElementById("signupForm");
    let logoutBtn = document.getElementById("logoutBtn");
    const storedName = localStorage.getItem("username");

    

    // افتراضياً، تحقق مما إذا كان هناك مستخدم مسجل دخول
    let storedEmail = localStorage.getItem("userEmail");


    if (logoutBtn) {
        let storedEmail = localStorage.getItem("userEmail");

        if (storedEmail) {
            logoutBtn.style.display = "inline-block"; // 🔹 إظهار زر تسجيل الخروج
        } else {
            logoutBtn.style.display = "none"; // 🔹 إخفاء زر تسجيل الخروج
        }

        logoutBtn.addEventListener("click", function() {
            let confirmLogout = confirm("هل تريد تسجيل الخروج؟");
            if (confirmLogout) {
                window.location.href = "signin.html"; // إعادة التوجيه
            }
        });
    }
    if (preferencesForm) {
        preferencesForm.addEventListener("submit", function(event) {
            event.preventDefault();
            let field = document.getElementById("field").value;
            let recommendations = {
                ai: { text: "....." },
                data: { text: "....." },
                web: { text: "....." }
            };

            let resultDiv = document.getElementById("result");
            resultDiv.innerHTML = `
                <div class="result-card">
                    <h3>🎯 Personalized Recommendation</h3>
                    <p><strong> ${storedName},</strong> ${recommendations[field].text}</p>
                </div>
            `;
            resultDiv.style.display = "block";
        });  
        
    }

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            event.preventDefault();
            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;

            let storedEmail = localStorage.getItem("userEmail");
            let storedPassword = localStorage.getItem("userPassword");

            if (email === storedEmail && password === storedPassword) {
                alert("🎉 Welcome back!");
                window.location.href = "index.html"; 
            } else {
                alert("❌ Invalid email or password!");
            }
        });
    }

    if (signupForm) {
        signupForm.addEventListener("submit", function(event) {
            event.preventDefault();
            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;
             let name =document.getElementById("username").value;

          if (localStorage.getItem("userEmail") === email) {
          alert("❌ This email is already registered. Try logging in.");
           return;
          } 

            localStorage.setItem("userEmail", email);
            localStorage.setItem("userPassword", password);
            localStorage.setItem("username",name );

            alert("✅ Account created successfully! You can now log in.");
            window.location.href = "signin.html"; 
        });
    }
});

