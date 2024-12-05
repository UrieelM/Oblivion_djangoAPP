// Select the main image and all secondary images
const mainImage = document.querySelector(".main-image");
const otherImages = document.querySelectorAll(".other-image");

// Add click event listeners to all secondary images
otherImages.forEach((img) => {
  img.addEventListener("click", () => {
    console.log(img.src);
    // Update the source of the main image with the clicked image's source
    mainImage.src = img.src;
  });
});
