

const passwordInput = document.querySelector("#password");
const passwordConfirmInput = document.querySelector("#password_confirm");

const submitInput = document.querySelector("#submit_button");

passwordInput.addEventListener("input", (event) => {
    submitInput.disabled = passwordInput.value !== passwordConfirmInput.value;
});

passwordConfirmInput.addEventListener("input", (event) => {
    submitInput.disabled = passwordInput.value !== passwordConfirmInput.value;
});
