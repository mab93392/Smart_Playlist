window.addEventListener('load', () => {
    // establishes new user button object
    const new_user = document.querySelector('#new_user')

    // redirects to authorization page
    new_user.addEventListener('click', () => {
        location.href = 'http://127.0.0.1:5500/auth'
    })
})