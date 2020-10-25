import theme from '@nuxt/content-theme-docs'
const base = '/GithubPR/'

export default theme({
    target: 'static',
    router: {
        base
    },
    css: [
        './css/main.css'
    ],
    hooks: {
        "vue-renderer:ssr:templateParams": function (params) {
            // fix hash links when using router.base - https://github.com/nuxt/content/issues/376#issuecomment-702193217
            params.HEAD = params.HEAD.replace(`<base href="${base}">`, "");
        }
    },
    content: {
        liveEdit: false,
        markdown: {
            prism: {
                theme: 'prism-themes/themes/prism-dracula.css'
            }
        }
    }
})
