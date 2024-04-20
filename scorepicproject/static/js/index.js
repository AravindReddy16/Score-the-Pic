let image1 = document.querySelector(".image1");
let image2 = document.querySelector(".image2");
let votes1 = document.querySelector(".votes1");
let votes2 = document.querySelector(".votes2");
let upload = document.querySelector("#upload");
let close = document.querySelector("#close");
let upload_img = document.querySelector(".upload-content");
function display() {
  votes1.style.display = "flex";
  votes2.style.display = "flex";
}
image1.addEventListener("click", function () {
  display();
});
image2.addEventListener("click", function () {
  display();
});
upload.addEventListener("click", function () {
  upload_img.style.display = "flex";
});
close.addEventListener("click", function () {
  upload_img.style.display = "none";
});
