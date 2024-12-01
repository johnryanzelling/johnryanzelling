// main.js
import { prevText, nextText } from './textGallery.js';
import { prevImage, nextImage } from './imageGallery.js';

// Initialize gallery navigation
document.querySelector(".arrow.left").addEventListener("click", prevText);
document.querySelector(".arrow.right").addEventListener("click", nextText);
document.querySelector(".image-gallery .arrow.left").addEventListener("click", prevImage);
document.querySelector(".image-gallery .arrow.right").addEventListener("click", nextImage);
