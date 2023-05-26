// burger
let burger = document.querySelector(".burger");
let menu = document.querySelector(".header__list__wrapper");
let menuLinks = document.querySelectorAll(".header__item__link");
let burgerClose = document.querySelector('.burger__close_btn');

burger.addEventListener('click',

    function () {
      burger.classList.toggle('burger--active');
      menu.classList.toggle('header__list__wrapper--active');
      document.body.classList.toggle('stop-scroll');

})

menuLinks.forEach(function (el){
  el.addEventListener('click', function (){
    burger.classList.remove('burger--active');
    menu.classList.remove('header__list__wrapper--active');
    document.body.classList.remove('stop-scroll');
  })
})
document.querySelector('.burger__close_btn').addEventListener("click", function() {
  document.querySelector('.header__list__wrapper').classList.remove('header__list__wrapper--active');
  document.body.classList.remove('stop-scroll');
})
// burger
// tabs
let tabsBtnNew = document.querySelectorAll('.how-we-work__list__item__link')
let tabsItemNew = document.querySelectorAll('.tab-item')

tabsBtnNew.forEach(function(elem){
  elem.addEventListener('click', function(e) {
    const path = e.currentTarget.dataset.path;

    tabsBtnNew.forEach(function(btn){btn.classList.remove('how-we-work--active')});
    e.currentTarget.classList.add('how-we-work--active');

    tabsItemNew.forEach(function(elem){elem.classList.remove('tab--active')});
    document.querySelector(`[data-target="${path}"]`).classList.add('tab--active');
  });
});
// tabs
// slider
const container = document.querySelector(".hero__container__content")
const swiper = new Swiper('.swiper', {

  speed: 300,
  pagination: {
    el: '.hero__pagination',
    type: 'bullets',
    clickable: true
  }

});
// slider
// search
document.querySelector('.header__search-btn').addEventListener('click', function () {
  document.querySelector('.header__search__form').classList.add('search__form__input__active');
  this.classList.add('active');
});

document.addEventListener('click', function(e) {
  let target = e.target;
  let form = this.document.querySelector('.header__search__form');
  if (!target.closest('.form-container')) {
  form.classList.remove('search__form__input__active');
    form.querySelector('search__form__input').value = "";
    document.querySelector('.header__search-btn').classList.remove('active');
  }
})
document.querySelector('.search__form__close').addEventListener("click", function() {
  document.querySelector('.header__search__form').classList.remove('search__form__input__active');
});
// search
// accordion
new Accordion('.accordion-list', {
  elementClass: 'accordion',
  triggerClass: 'accordion__control',
  panelClass: 'accordion__content',
  activeClass: 'accordion--active'
});
// accordion
