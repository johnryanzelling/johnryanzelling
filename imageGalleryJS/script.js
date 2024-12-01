const images = [
    "images/curvePlotsimg.png",
    "images/gantO1.png",
    "images/gantO2.png",
    "images/logarithmic.png",
    "images/rotationSolid01.png",
    "images/rotationSolid02.png",
    "images/toroidal.png",
    "images/trefoil.png",
    "images/ucc_seed1.png",
    "images/ucc_seed2.png",
    "images/ucc_seed3.png",
    "images/ucc_seed4.png",
    "images/ucc_seed5.png",
    "images/ucc_seed6.png",
    "images/ucc_seed7.png",
    "images/ucc_seed8.png"
];

const galleryContainer = document.querySelector(".image-container");
const fileNameContainer = document.getElementById("file-name");
let currentIndex = 0;

// Dynamically add images to the gallery
const imgElements = images.map((image, index) => {
    const imgElement = document.createElement("img");
    imgElement.src = image;
    imgElement.alt = `Image ${index + 1}`;
    if (index === 0) imgElement.classList.add("active");
    galleryContainer.appendChild(imgElement);
    return imgElement;
});

// Function to show the current image and update the file name
function showImage(index) {
    imgElements.forEach((img, i) => {
        img.classList.toggle("active", i === index);
    });
    fileNameContainer.textContent = images[index].split("/").pop(); // Extract file name
}

// Initial setup
showImage(currentIndex);

// Navigation functions
function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
}
