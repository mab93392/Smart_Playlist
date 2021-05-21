window.addEventListener('load', () => {
    // establishes button objects
    const new_user = document.querySelector('#new_user')
    const create_playlist = document.querySelector('#create')

    // redirects to playlist page
    create_playlist.addEventListener('click', () => {
        location.href = 'http://127.0.0.1:5500/playlist'
    })

    // redirects to authorization page
    new_user.addEventListener('click', () => {
        location.href = 'http://127.0.0.1:5500/auth'
    })
})