const iframe = document.querySelector(".map-content iframe");

iframe.onload = () => {
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    const canvas = iframeDoc.querySelector("canvas");

    if (canvas) {
        const ctx = canvas.getContext("2d", { willReadFrequently: true });
        console.log("Canvas encontrado e configurado!");
    } else {
        console.error("Canvas não encontrado dentro do iframe.");
    }
};
