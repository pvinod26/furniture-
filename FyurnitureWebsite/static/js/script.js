/* ===========================================
            WELCOME PAGE
=========================================== */

function continueToHome(event){

    event.preventDefault();

    const customerName = document
        .getElementById("customerName")
        .value
        .trim();

    if(customerName === ""){

        alert("Please enter your name.");

        return;

    }

    sessionStorage.setItem("customerName", customerName);

    window.location.href = "/home";

}


/* ===========================================
            HOME PAGE
=========================================== */

function loadCustomerName(){

    const customerName = sessionStorage.getItem("customerName");

    if(customerName){

        const element = document.getElementById("welcomeUser");

        if(element){

            element.innerHTML =
            `Welcome, <span style="color:#7B4F35;">${customerName}</span>`;

        }

    }

}


/* ===========================================
            PRODUCT PAGE
=========================================== */

function sendWhatsApp(){

    const customerName =
        sessionStorage.getItem("customerName") || "Customer";

    const productName =
        document.getElementById("productName").innerText;

    const productPrice =
        document.getElementById("productPrice").innerText;

    const productImage =
        document.getElementById("productImage").src;

    const productId =
        document.getElementById("productId").innerText;

    const material =
        document.getElementById("material").innerText;

    const message =

`Hello,

My name is ${customerName}.

I am interested in the following furniture.

🛋 Product : ${productName}

🆔 Product ID : ${productId}

🪵 Material : ${material}

💰 Price : ${productPrice}

📷 Product Image :

${productImage}

Please share more details regarding availability and delivery.

Thank you.`;

    const phone = "919876543210";

    window.open(

        `https://wa.me/${phone}?text=${encodeURIComponent(message)}`,

        "_blank"

    );

}


/* ===========================================
            IMAGE GALLERY
=========================================== */

function changeImage(image){

    document.getElementById("productImage").src = image.src;

}


/* ===========================================
            PAGE LOAD
=========================================== */

document.addEventListener("DOMContentLoaded",function(){

    loadCustomerName();

});