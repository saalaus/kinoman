document.addEventListener("DOMContentLoaded", () => {
    // MENU BURGER
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(
        document.querySelectorAll(".navbar-burger"),
        0
    );

    // Add a click event on each of them
    $navbarBurgers.forEach((el) => {
        el.addEventListener("click", () => {
            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle("is-active");
            $target.classList.toggle("is-active");
        });
    });

    // REGISTER MODAL
    const $modal = document.getElementById("modal-login")
    const $register_btn_tab = document.getElementById("go-registration")
    const $login_btn_tab = document.getElementById("go-login")
    const $login_page = document.getElementById("page-login")
    const $register_page = document.getElementById("page-register")
    function openModal(mode){
        mode = mode?mode:0
        $modal.classList.add("is-active")
        toggleTab(mode)
    }
    function closeModal(){
        $modal.classList.remove("is-active")
        location.hash = ""
    }
    function toggleTab(mode){
        mode = mode?mode:0
        if (mode === 0){
            $register_btn_tab.classList.add("is-active")
            $login_btn_tab.classList.remove("is-active")
            $login_page.style.display = "none"
            $register_page.style.display = "block"
        }
        if (mode === 1){
            $register_btn_tab.classList.remove("is-active")
            $login_btn_tab.classList.add("is-active")
            $login_page.style.display = "block"
            $register_page.style.display = "none"
        }
    }

    const $register_btn = document.getElementById("open-register")
    const $login_btn = document.getElementById("open-login")
    $register_btn.addEventListener("click", () => openModal(0))
    $register_btn_tab.addEventListener("click", () => toggleTab(0))
    $login_btn_tab.addEventListener("click", () => toggleTab(1))
    $login_btn.addEventListener("click", () => openModal(1))
    document.getElementById("modal-close").addEventListener("click", closeModal)


    // open modal on page load
    if (location.hash === "#register") openModal(0)
    if (location.hash === "#login") openModal(1)
});
