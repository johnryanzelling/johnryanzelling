// imageGallery.js
import { toggleActiveClass } from './gallery.js';

const imagesList = [
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
    "images/ucc_seed8.png",
];

const galleryContainer = document.querySelector(".image-gallery");
imagesList.forEach((src, index) => {
    const img = document.createElement("img");
    img.src = src;
    img.alt = `Image ${index + 1}`;
    if (index === 0) img.classList.add("active"); // First image is active by default
    galleryContainer.insertBefore(img, galleryContainer.querySelector(".arrow.right"));
});

// Select all images for navigation
const images = document.querySelectorAll(".image-gallery img");
let currentImageIndex = 0;

function showImage(index) {
    toggleActiveClass(images, index);
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    showImage(currentImageIndex);
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    showImage(currentImageIndex);
}

export { prevImage, nextImage };
