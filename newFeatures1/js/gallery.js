// gallery.js

// Helper function to handle active state toggling
function toggleActiveClass(items, index) {
    items.forEach((item, i) => {
        item.classList.toggle("active", i === index);
    });
}

export { toggleActiveClass };
