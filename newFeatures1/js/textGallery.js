// textGallery.js
import { toggleActiveClass } from './gallery.js';

const textItems = document.querySelectorAll(".text-content h3");
let currentTextIndex = 0;

function showText(index) {
    toggleActiveClass(textItems, index);
}

function prevText() {
    currentTextIndex = (currentTextIndex - 1 + textItems.length) % textItems.length;
    showText(currentTextIndex);
}

function nextText() {
    currentTextIndex = (currentTextIndex + 1) % textItems.length;
    showText(currentTextIndex);
}

export { prevText, nextText };
