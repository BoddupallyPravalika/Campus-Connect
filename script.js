const scroll = new LocomotiveScroll({
    el: document.querySelector('#main'),
    smooth: true
});
var elemC = document.querySelector("#elem-container")
var fixed = document.querySelector("#fixed-image")
elemC.addEventListener("mouseenter",function(){
   fixed.style.display = "block"
})
elemC.addEventListener("mouseleave",function(){
    fixed.style.display = "none"
 })
 
 var elems = document.querySelectorAll(".elem")
 elems.forEach(function(e){
    e.addEventListener("mouseenter",function(){
        var image = e.getAttribute("data-image")
        fixed.style.backgroundImage = `url(${image})`
    })
 })
 document.addEventListener("DOMContentLoaded", function() {
    var elems = document.querySelectorAll('.elem');
    var urls = {
        'Hackathons': 'hackathons.html',
        'Tech Talks': 'tech_talks.html',
        'Seminars': 'seminars.html',
        'Coding Competitions': 'coding_competitions.html',
        'Technical Workshops': 'technical_workshops.html',
        'Project Exhibitions': 'project_exhibitions.html',
        'Cultural Festivals': 'cultural_festivals.html',
        'Sports Tournaments': 'sports_tournaments.html',
        'Debates and Quiz Competitions': 'debates_quiz.html',
        'Cultural Workshops': 'cultural_workshops.html',
        'Social Impact Initiatives': 'social_impact_activities.html'
    };
    elems.forEach(function(elem) {
        elem.addEventListener('click', function() {
            var text = elem.querySelector('h2, h3, h4, h5, h6, h7, h8, h9, h10').textContent.trim();
            if (text in urls) {
                window.location.href = urls[text];
            } else {
                console.error('Page URL not found for: ' + text);
            }
        });
    });
});
function swiperAnimation(){
var swiper = new Swiper(".mySwiper", {
    slidesPerView: "auto",
    centeredSlides: true,
    spaceBetween: 70,
  });
}
swiperAnimation()
var loader = document.querySelector("#loader");
var h1Elements = document.querySelectorAll("#loader h1");
function animateH1s() {
    var delayBetweenWords = 1000; 
    h1Elements.forEach((h1, index) => {
        setTimeout(() => {
            h1.style.opacity = 1;
            setTimeout(() => {
                h1.style.opacity = 0;
            }, 500);
        }, index * (delayBetweenWords + 500));
    });
    setTimeout(() => {
        loader.style.top = "-100%";
    }, h1Elements.length * (delayBetweenWords + 500));
}
animateH1s();
document.addEventListener("DOMContentLoaded", function() {
    // Check if the loader has been shown before
    if (!sessionStorage.getItem('loaderShown')) {
        // Show the loader
        document.getElementById('loader').style.display = 'flex';

        // Set a timeout to hide the loader after a certain period
        setTimeout(function() {
            document.getElementById('loader').style.opacity = '0';
            setTimeout(function() {
                document.getElementById('loader').style.display = 'none';
            }, 1000); // 1 second to match the transition duration
        }, 2000); // Show loader for 2 seconds

        // Mark the loader as shown in session storage
        sessionStorage.setItem('loaderShown', 'true');
    } else {
        // Hide the loader if it has been shown before
        document.getElementById('loader').style.display = 'none';
    }
});



