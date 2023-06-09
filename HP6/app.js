const arrows = document.querySelectorAll(".arrow");
const movieLists = document.querySelectorAll(".movie-list");

arrows.forEach((arrow, i) => {
  
  const itemNumber = movieLists[i].querySelectorAll("img").length;
  const maxWidth = itemNumber * 200;
  let initialWidth = 6 * 200;
  arrow.addEventListener("click", (event) => {
    console.log(window.innerWidth)
    const movieList = $($(event.target).prev()[0])
    if(initialWidth === maxWidth){
      movieList.css("margin-left", "0px")
      initialWidth = 1200;
    }
    else {
      marginLeft = parseInt($(movieList).css("marginLeft"))
      initialWidth += 200;
      movieList.css("margin-left", `${marginLeft - 200}px`)
    }

  });
});

//TOGGLE

const ball = document.querySelector(".toggle-ball");
const items = document.querySelectorAll(
  ".container,.movie-list-title,.navbar-container,.sidebar,.left-menu-icon,.toggle"
);

ball.addEventListener("click", () => {
  items.forEach((item) => {
    item.classList.toggle("active");
  });
  ball.classList.toggle("active");
});
