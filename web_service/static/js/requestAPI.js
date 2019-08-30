/**
 * Sending raw file analyzing to server
 *
 * @param {*} requestData
 * @param {*} options
 */
const uploadRawFileRequest = (requestData, options) => {
    const formData = new FormData();

    const { rawFile, hotelAccount } = requestData;

    formData.append('rawFile', rawFile);
    formData.append('hotelAccount', hotelAccount);

    return fetch('/upload/rawData', {
        method: 'POST',
        body: formData,
        ...options
    });
};

/**
 * Sending analyze request to server and get the response
 *
 *
 * @param {{fromDate, toDate, hotelAccount, analyzeOptions}} requestData
 * @param {*} options options sent along with request
 *
 * @returns {Promise} which have reponse from fetch
 */
const analyzeRequest = (requestData, options) => {
    const formData = new FormData();

    const { fromDate, toDate, hotelAccount, analyzeOptions } = requestData;

    let urlAnalyze = '/analyze/analyzeDetail';

    if (analyzeOptions === 'DB') {
        urlAnalyze = '/analyze/analyzeDatabase';
    }

    formData.append('fromDate', fromDate);
    formData.append('toDate', toDate);
    formData.append('hotelAccount', hotelAccount);
    formData.append('analyzeOptions', analyzeOptions);

    return fetch(urlAnalyze, {
        method: 'POST',
        body: formData,
        ...options
    });
};
