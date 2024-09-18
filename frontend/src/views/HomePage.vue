<template>
  <div id="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container hero-container">
        <div class="hero-content">
          <h1 class="hero-title">Dawlat Emad</h1>
          <p class="hero-subtitle">
            Your Journey to Self-Discovery and Success Starts Here
          </p>
          <!-- Changed @click event to openStory -->
          <button class="hero-button" @click="openStory">My Story</button>
        </div>
        <div class="hero-image-wrapper">
          <img
            src="@/assets/images/dawlat.png"
            alt="Dawlat Emad"
            class="hero-image"
          />
        </div>
      </div>
      <div class="scroll-indicator" @click="scrollToContent">
        <span></span>
      </div>
    </section>

    <!-- Added Story Widget -->
    <div
      class="story-widget"
      v-if="showStory"
      @click.self="closeStory"
    >
      <div class="story-content">
        <button class="close-button" @click="closeStory">&times;</button>
        <h2 class="story-title">About Dawlat Emad</h2>
        <p class="story-text">
          <!-- Replace this text with Dawlat's actual story -->
          Dawlat Emad is a passionate life coach dedicated to helping individuals discover their true potential and achieve their dreams. With years of experience in personal development, Dawlat provides insightful guidance and support to empower others on their journey to self-improvement.
        </p>
      </div>
    </div>
    <!-- Services Section -->
    <section class="services">
      <div class="container">
        <h2
          class="section-title"
          :class="{ 'animate-slide-up': servicesVisible }"
        >
          Services I Offer
        </h2>
        <div class="services-grid">
          <div
            class="service-card"
            v-for="(service, index) in services"
            :key="index"
            :class="{ 'animate-fade-in': servicesVisible }"
          >
            <i :class="service.icon + ' service-icon'"></i>
            <h3 class="service-title">{{ service.title }}</h3>
            <p class="service-description">{{ service.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
      <div class="container">
        <h2
          class="section-title"
          :class="{ 'animate-slide-left': testimonialsVisible }"
        >
          What My Clients Say
        </h2>
        <div
          class="testimonials-slider"
          :class="{ 'animate-fade-in': testimonialsVisible }"
        >
          <div
            class="testimonial-card"
            v-for="(testimonial, index) in testimonials"
            :key="index"
          >
            <p class="testimonial-quote">"{{ testimonial.quote }}"</p>
            <h4 class="testimonial-author">- {{ testimonial.author }}</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact">
      <div class="container">
        <h2
          class="section-title"
          :class="{ 'animate-slide-up': contactVisible }"
        >
          Get in Touch
        </h2>
        <p
          class="section-text"
          :class="{ 'animate-fade-in': contactVisible }"
        >
          Ready to take the next step? Let's connect and start your journey.
        </p>
        <button
          class="contact-button"
          @click="bookSession"
          :class="{ 'animate-zoom-in': contactVisible }"
        >
          Book a Session
        </button>
      </div>
    </section>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';

export default {
  name: 'HomePage',
  setup() {
    // Reactive references for visibility states
    const heroVisible = ref(false);
    const servicesVisible = ref(false);
    const testimonialsVisible = ref(false);
    const contactVisible = ref(false);

    const services = ref([
      {
        icon: 'fas fa-user-circle',
        title: 'Personal Coaching',
        description: 'One-on-one sessions tailored to your unique needs and goals.',
      },
      {
        icon: 'fas fa-users',
        title: 'Group Workshops',
        description: 'Engaging group sessions to foster community and shared learning.',
      },
      {
        icon: 'fas fa-building',
        title: 'Corporate Training',
        description:
          'Custom training programs for organizations aiming to improve team dynamics and leadership skills.',
      },
    ]);

    const testimonials = ref([
      {
        quote: 'Dawlat helped me find clarity and purpose in my life.',
        author: 'Aya',
      },
      {
        quote: "The best investment I've made in myself. Highly recommend!",
        author: 'John Doe',
      },
      {
        quote: 'Her guidance has been transformative in both my personal and professional life.',
        author: 'Jane Smith',
      },
    ]);

    // Define the bookSession function to handle the button click
    const bookSession = () => {
      console.log("Redirecting to the booking page...");
      // You can add navigation here or open a modal
      // Example to redirect to booking page:
      // this.$router.push('/booking');
    };

    const scrollToContent = () => {
      const nextSection = document.querySelector('.services');
      if (nextSection) {
        nextSection.scrollIntoView({ behavior: 'smooth' });
      }
    };

    const handleScroll = () => {
      const scrollY = window.scrollY + window.innerHeight;

      const heroSection = document.querySelector('.hero');
      const servicesSection = document.querySelector('.services');
      const testimonialsSection = document.querySelector('.testimonials');
      const contactSection = document.querySelector('.contact');

      if (heroSection && scrollY > heroSection.offsetTop) {
        heroVisible.value = true;
      }
      if (servicesSection && scrollY > servicesSection.offsetTop + 100) {
        servicesVisible.value = true;
      }
      if (testimonialsSection && scrollY > testimonialsSection.offsetTop + 100) {
        testimonialsVisible.value = true;
      }
      if (contactSection && scrollY > contactSection.offsetTop + 100) {
        contactVisible.value = true;
      }
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
      handleScroll(); // Initial check in case the user reloads halfway down
    });

    return {
      heroVisible,
      servicesVisible,
      testimonialsVisible,
      contactVisible,
      services,
      testimonials,
      bookSession, // Make sure bookSession is returned here
      scrollToContent,
    };
  },
};
</script>


<style scoped>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap');

/* Reset and General Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
  color: #333;
  background-color: #f9f9f9;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  cursor: pointer;
  border: none;
  outline: none;
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: auto;
}

/* Section Titles */
.section-title {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
}

/* Hero Section */
.hero {
  position: relative;
  height: 100vh;
  background-image: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.6),
      rgba(0, 0, 0, 0.6)
    ),
    url('@/assets/images/hero-background.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  color: #fff;
}

.hero-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.hero-content {
  flex: 1;
}

.hero-title {
  font-size: 4rem;
  margin-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  line-height: 1.5;
}

.hero-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 1rem 2rem;
  border-radius: 50px;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
}

.hero-button:hover {
  background-color: #e65b50;
}

.hero-image-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
}

.hero-image {
  border-radius: 50%;
  width: 350px;
  height: 350px;
  object-fit: cover;
  border: 5px solid #fff;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

/* Scroll Indicator */
.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  cursor: pointer;
}

.scroll-indicator span {
  display: block;
  width: 30px;
  height: 30px;
  border-bottom: 3px solid #fff;
  border-right: 3px solid #fff;
  transform: rotate(45deg);
  animation: scrollDown 2s infinite;
}

@keyframes scrollDown {
  0% {
    transform: translateX(-50%) rotate(45deg) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) rotate(45deg) translateY(15px);
    opacity: 0;
  }
}

/* Services Section */
.services {
  padding: 5rem 0;
  background-color: #fff;
}

.services-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.service-card {
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 15px;
  width: 350px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.service-icon {
  font-size: 3rem;
  color: #ff6f61;
  margin-bottom: 1rem;
}

.service-title {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
}

.service-description {
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
}

/* Testimonials Section */
.testimonials {
  padding: 5rem 0;
  background-color: #f1f1f1;
}

.testimonials-slider {
  display: flex;
  gap: 2rem;
  overflow-x: auto;
  padding-bottom: 1rem;
  scroll-snap-type: x mandatory;
}

.testimonial-card {
  background-color: #fff;
  padding: 2rem;
  border-radius: 10px;
  min-width: 300px;
  flex: none;
  scroll-snap-align: start;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.testimonial-quote {
  font-size: 1.2rem;
  font-style: italic;
  margin-bottom: 1rem;
  color: #333;
}

.testimonial-author {
  font-size: 1rem;
  font-weight: bold;
  color: #ff6f61;
}

/* Contact Section */
.contact {
  padding: 5rem 0;
  background-color: #ff6f61;
  color: #fff;
  text-align: center;
}

.contact-button {
  background-color: #fff;
  color: #ff6f61;
  padding: 1rem 2.5rem;
  border-radius: 50px;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
}

.contact-button:hover {
  background-color: #f1f1f1;
}

/* Animations */
.animate-fade-in {
  animation: fadeIn 1s forwards;
}

.animate-slide-up {
  animation: slideUp 1s forwards;
}

.animate-slide-left {
  animation: slideLeft 1s forwards;
}

.animate-zoom-in {
  animation: zoomIn 1s forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Responsive Design */
@media (max-width: 992px) {
  .hero-container {
    flex-direction: column-reverse;
    text-align: center;
  }

  .hero-content,
  .hero-image-wrapper {
    flex: none;
    width: 100%;
  }

  .hero-image {
    width: 250px;
    height: 250px;
    margin-bottom: 2rem;
  }
}

@media (max-width: 768px) {
  .service-card {
    width: 100%;
  }

  .testimonials-slider {
    flex-direction: column;
    align-items: center;
  }
}


/* Story Widget Styles */
.story-widget {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  overflow-y: auto;
  z-index: 1000;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  opacity: 0;
  animation: fadeIn 0.5s forwards;
}

.story-content {
  background-color: #fff;
  width: 100%;
  max-width: 600px;
  max-height: 90%;
  padding: 2rem;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  overflow-y: auto;
  transform: translateY(100%);
  animation: slideUp 0.5s forwards;
}

.close-button {
  background: none;
  border: none;
  font-size: 2rem;
  font-weight: bold;
  position: absolute;
  top: 1rem;
  right: 1rem;
  cursor: pointer;
}

.story-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: #333;
}

.story-text {
  font-size: 1rem;
  line-height: 1.6;
  color: #555;
}

/* Animations */
@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  to {
    transform: translateY(0);
  }
}

/* Modal Styles */
.story-modal {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  animation: fadeIn 0.3s ease-out forwards;
}

.story-modal-content {
  background-color: #fff;
  width: 100%;
  max-width: 600px;
  border-radius: 20px 20px 0 0;
  padding: 2rem;
  position: relative;
  transform: translateY(100%);
  animation: slideUp 0.4s ease-out forwards;
}

.close-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
}

.story-title {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.story-text {
  font-size: 1.2rem;
  line-height: 1.6;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}


/* Ensure the content doesn't scroll when the widget is open */
body.no-scroll {
  overflow: hidden;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .story-content {
    width: 100%;
    border-radius: 20px 20px 0 0;
  }
}

/* Story Widget Styles */
.story-widget {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  overflow-y: auto;
  z-index: 1000;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  opacity: 0;
  animation: fadeIn 0.5s forwards;
}

.story-content {
  background-color: #fff;
  width: 100%;
  max-width: 600px;
  max-height: 90%;
  padding: 2rem;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  overflow-y: auto;
  transform: translateY(100%);
  animation: slideUp 0.5s forwards;
  position: relative;
}

.close-button {
  background: none;
  border: none;
  font-size: 2rem;
  font-weight: bold;
  position: absolute;
  top: 1rem;
  right: 1rem;
  cursor: pointer;
}

.story-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: #333;
}

.story-text {
  font-size: 1rem;
  line-height: 1.6;
  color: #555;
}

/* Animations */
@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  to {
    transform: translateY(0);
  }
}

/* Responsive Styles */
@media (max-width: 768px) {
  .story-content {
    width: 100%;
    border-radius: 20px 20px 0 0;
  }
}
</style>



