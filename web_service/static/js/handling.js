ready(() => {
    document
        .querySelector('input[name=raw-data]')
        .addEventListener('change', () => {
            // Update file name from input file to label
            const rawDataFileName = document.querySelector(
                'input[name=raw-data]'
            ).files[0].name;

            document.querySelector(
                'label[tag=raw-data]'
            ).innerHTML = rawDataFileName;
        });
});

/**
 * Upload raw File to server. Data in raw file will be saved into database.
 * This function will also change the flash message.
 *
 *
 */
const uploadRawFile = async () => {
    const inputRawFileObject = document.querySelector('input[name=raw-data]');
    const rawFile = inputRawFileObject.files[0];

    const hotelAccount = document.querySelector('[name=hotel-account]').value;

    const flashMessage = makeFlashMessage('.flash-message');
    flashMessage.setText('Uploading', 'loading');

    try {
        const result = await uploadRawFileRequest({
            rawFile,
            hotelAccount
        });

        if (result.status == 200) {
            flashMessage.setText('Completed');
        } else {
            flashMessage.setText('Error happened !!!');
        }
    } catch (err) {
        console.error(err);
        flashMessage.setText('Error happened !!!');
    }
};

// When click to analyze raw data button
const analyzeRaw = async () => {
    const fromDate = document.querySelector('input[name=analyze-date-from]')
        .value;
    const toDate = document.querySelector('input[name=analyze-date-to]').value;
    const hotelAccount = document.querySelector('[name=hotel-account]').value;

    const flashMessage = makeFlashMessage('.flash-message');
    flashMessage.setText('Analyzing raw data', 'loading');

    try {
        const analyzeResult = await analyzeRequest({
            fromDate,
            toDate,
            hotelAccount
        });

        if (analyzeResult.status == 200) {
            flashMessage.setText('Completed');
        } else {
            flashMessage.setText('Error happened !!!');
        }
    } catch (err) {
        console.log(err);
        flashMessage.setText('Error happened !!!');
    }
};

// When click to analyze database button
const analyzeDB = async () => {
    const fromDate = document.querySelector('input[name=analyze-date-from]')
        .value;
    const toDate = document.querySelector('input[name=analyze-date-to]').value;
    const hotelAccount = document.querySelector('[name=hotel-account]').value;

    const flashMessage = makeFlashMessage('.flash-message');
    flashMessage.setText('Analyzing database data', 'loading');

    try {
        const analyzeResult = await analyzeRequest({
            fromDate,
            toDate,
            hotelAccount,
            analyzeOptions: 'DB'
        });

        if (analyzeResult.status == 200) {
            flashMessage.setText('Completed');
        } else {
            flashMessage.setText('Error happened !!!');
        }
    } catch (err) {
        console.log(err);
        flashMessage.setText('Error happened !!!');
    }
};
