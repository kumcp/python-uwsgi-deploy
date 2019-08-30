const makeFlashMessage = selector => {
    const flashMessageDOM = document.querySelector(selector);
    const wrapperDOM = flashMessageDOM.querySelector('.flash-message-wrapper');

    const loading =
        '<div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>';

    return {
        flashMessageDOM,
        selector,
        wrapperDOM,
        setText(text, type) {
            this.wrapperDOM.innerHTML = `<strong>${text}</strong>`;

            if (type == 'loading') {
                this.wrapperDOM.innerHTML += loading;
            }
        },
        getText() {
            return this.wrapperDOM.querySelector("strong").innerHTML;
        }
    };
};
