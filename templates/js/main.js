document.querySelector(".form-file__input").addEventListener("change", function () {
    if (this.files[0]) {
        var fr = new FileReader();

        fr.addEventListener("load", function () {
            document.querySelector(".img").style.display = 'block';
            document.querySelector(".form-file__close").style.display = 'block';
            document.querySelector(".img").style.backgroundImage = "url(" + fr.result + ")";
            document.querySelector(".form-file__choose").style.display = 'none';
        }, false);

        fr.readAsDataURL(this.files[0]);
    }
});

document.querySelector(".form-file__close").addEventListener("click", function () {
    document.querySelector(".img").style.display = 'none';
    document.querySelector(".form-file__close").style.display = 'none';
    document.querySelector(".form-file__choose").style.display = 'inline';
    document.querySelector('.form-file__input').value = '';
});

window.onload = function () {
    document.getElementById("btn_add-article").style.display = "none";
};