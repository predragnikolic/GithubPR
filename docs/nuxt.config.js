import theme from '@nuxt/content-theme-docs'
const base = '/GithubPR/'

export default theme({
    target: 'static',
    router: {
        base
    },
    hooks: {
        "vue-renderer:ssr:templateParams": function (params) {
            // fix hash links when using router.base - https://github.com/nuxt/content/issues/376#issuecomment-702193217
            params.HEAD = params.HEAD.replace(`<base href="${base}">`, "");
        }
    }
})
