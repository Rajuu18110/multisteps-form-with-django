var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

let fullname = document.getElementById('fullname')
fullname.addEventListener('input', validatefullname)
function validatefullname() {
    if (fullname.value.length < 3) {
        fullname.style.color = 'red'
    }
    else {
        fullname.style.color = 'green'
    }
}
let adds = document.getElementById('adds')
adds.addEventListener('input', validateadds)
function validateadds() {
    if (adds.value.length < 12) {
        adds.style.color = 'red'
    }
    else {
        adds.style.color = 'green'
    }
}
let city = document.getElementById('city')
city.addEventListener('input', validatecity)
function validatecity() {
    if (city.value.length < 3) {
        city.style.color = 'red'
    }
    else {
        city.style.color = 'green'
    }
}
let state = document.getElementById('state')
state.addEventListener('input', validatestate)
function validatestate() {
    if (state.value.length < 3) {
        state.style.color = 'red'
    }
    else {
        state.style.color = 'green'
    }
}
let zip = document.getElementById('zip')
zip.addEventListener('input', validatezip)
function validatezip() {
    if (zip.value.length < 6) {
        zip.style.color = 'red'
    }
    else {
        zip.style.color = 'green'
    }
}
let mob = document.getElementById('mob')
mob.addEventListener('input', validatemob)
function validatemob() {
    if (mob.value.length < 10) {
        mob.style.color = 'red'
    }
    else {
        mob.style.color = 'green'
    }
}
let mail = document.querySelector("#mail")
mail.addEventListener('input', validatemail)
function validatemail() {
    const emailInputValue = document.getElementById("mail").value;
    if (/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(emailInputValue) != true) {
        mail.style.color = 'red'
    }
    else {
        mail.style.color = 'green'
    }
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, z, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].querySelectorAll("input:not(.novalidate)");
    z = x[currentTab].getElementsByTagName("textarea");

    a = document.getElementById('fullname')
    if (a.value.length < 3) {
        a.className += " invalid";
        valid = false;
    }
    else {
        a.style.color = 'green'
    }

    b = document.getElementById('adds')
    if (b.value.length < 12) {
        b.className += " invalid";
        valid = false;
    }
    else {
        b.style.color = 'green'
    }

    c = document.getElementById('city')
    if (c.value.length < 3) {
        c.className += " invalid";
        valid = false;
    }
    else {
        c.style.color = 'green'
    }

    d = document.getElementById('state')
    if (d.value.length < 3) {
        d.className += " invalid";
        valid = false;
    }
    else {
        d.style.color = 'green'
    }

    e = document.getElementById('zip')
    if (e.value.length < 6) {
        e.className += " invalid";
        valid = false;
    }
    else {
        e.style.color = 'green'
    }

    f = document.getElementById('mob')
    if (f.value.length < 10) {
        f.className += " invalid";
        valid = false;
    }
    else {
        f.style.color = 'green'
    }
    
    let g = document.querySelector("#mail")
    const emailInputValue = document.getElementById("mail").value;
    if (/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(emailInputValue) != true) {
        g.className += " invalid";
        valid = false;
    }
    else {
        g.style.color = 'green'
    }

    h = document.getElementById('dob')
    if (h.value.length < 6) {
        h.className += " invalid";
        valid = false;
    }
    else {
        h.style.color = 'green'
    }
    
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    for (i = 0; i < z.length; i++) {
        // If a field is empty...
        if (z[i].value == "") {
            // add an "invalid" class to the field:
            z[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

function onlyNumberKey(evt) {
    // Only ASCII character in that range allowed
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
        return false;
    return true;
}

function ValidateAlpha(evt) {
    var keyCode = (evt.which) ? evt.which : evt.keyCode
    if ((keyCode < 65 || keyCode > 90) && (keyCode < 97 || keyCode > 123) && keyCode != 32)
        return false;
    return true;
}

let pass = document.getElementById('passyr')
pass.addEventListener('input', validatepass)
function validatepass() {
    if (pass.value.length < 4) {
        pass.style.color = 'red'
    }
    else {
        pass.style.color = 'green'
    }
}

function EnableDisableTextBox() {
    var y1 = document.getElementById("y1");
    var applicationdate = document.getElementById("applicationdate");
    applicationdate.disabled = y1.checked ? false : true;
    if (!applicationdate.disabled) {
        applicationdate.focus();
    }
}
function EnableDisableTextBox2() {
    var y3 = document.getElementById("y3");
    var feedata = document.getElementById("feedata");
    feedata.disabled = y3.checked ? false : true;
    if (!feedata.disabled) {
        feedata.focus();
    }
}