require.config({
    paths: {
        "axios": "lib/axios.min",
        "marked": "lib/marked.min",
        "vue": "lib/vue.min"
    },
    shim: {
        //
    },
    config: {
        babel: {
            sourceMaps: "inline",
            fileExtension: ".js,.jsx",
            compact: false
        }
    }
});

require([
    "./view/index"
]);
