document.addEventListener('DOMContentLoaded', () => {
    const slideContainers = document.querySelectorAll('.slides');

    slideContainers.forEach(container => {
        const items = Array.from(container.children);
        items.forEach(item => {
            const clone = item.cloneNode(true);
            clone.setAttribute('aria-hidden', 'true');
            container.appendChild(clone);
        });
    });
});