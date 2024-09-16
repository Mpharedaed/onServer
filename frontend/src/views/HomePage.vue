<template>
  <div id="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title" :class="{ 'animate-fade-in': heroVisible }">Dawlat Emad</h1>
          <p class="hero-subtitle" :class="{ 'animate-slide-up': heroVisible }">Your Journey to Self-Discovery and Success Starts Here</p>
          <button class="hero-button" @click="bookSession" :class="{ 'animate-zoom-in': heroVisible }">Book a Session</button>
        </div>
        <div class="hero-image-wrapper" :class="{ 'animate-fade-in': heroVisible }">
          <img src="@/assets/images/dawlat.png" alt="Dawlat Emad" class="hero-image" />
        </div>
      </div>
      <div class="scroll-indicator" @click="scrollToContent">
        <span></span>
      </div>
    </section>

    <!-- Introduction Section -->
    <section class="introduction">
      <div class="container">
        <h2 class="section-title" :class="{ 'animate-slide-left': introVisible }">Welcome to My Coaching Space</h2>
        <p class="section-text" :class="{ 'animate-slide-right': introVisible }">
          I’m Dawlat Emad, a certified life coach dedicated to helping you achieve your personal and professional goals. Together, we can navigate the challenges of life, unlock your potential, and build the life you’ve always dreamed of.
        </p>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services">
      <div class="container">
        <h2 class="section-title" :class="{ 'animate-slide-up': servicesVisible }">Services I Offer</h2>
        <div class="services-grid">
          <div class="service-card" v-for="(service, index) in services" :key="index" :class="{ 'animate-fade-in': servicesVisible }">
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
        <h2 class="section-title" :class="{ 'animate-slide-left': testimonialsVisible }">What My Clients Say</h2>
        <div class="testimonials-slider" :class="{ 'animate-fade-in': testimonialsVisible }">
          <div class="testimonial-card" v-for="(testimonial, index) in testimonials" :key="index">
            <p class="testimonial-quote">"{{ testimonial.quote }}"</p>
            <h4 class="testimonial-author">- {{ testimonial.author }}</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact">
      <div class="container">
        <h2 class="section-title" :class="{ 'animate-slide-up': contactVisible }">Get in Touch</h2>
        <p class="section-text" :class="{ 'animate-fade-in': contactVisible }">Ready to take the next step? Let's connect and start your journey.</p>
        <button class="contact-button" @click="bookSession" :class="{ 'animate-zoom-in': contactVisible }">Book a Session</button>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  name: 'HomePage',
  setup() {
    const heroVisible = ref(false);
    const introVisible = ref(false);
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
        description: 'Custom training programs for organizations aiming to improve team dynamics and leadership skills.',
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

    const bookSession = () => {
      // Implement booking session functionality
    };

    const scrollToContent = () => {
      const nextSection = document.querySelector('.introduction');
      nextSection.scrollIntoView({ behavior: 'smooth' });
    };

    const handleScroll = () => {
      const scrollY = window.scrollY + window.innerHeight;

      if (scrollY > document.querySelector('.hero').offsetTop) {
        heroVisible.value = true;
      }
      if (scrollY > document.querySelector('.introduction').offsetTop + 100) {
        introVisible.value = true;
      }
      if (scrollY > document.querySelector('.services').offsetTop + 100) {
        servicesVisible.value = true;
      }
      if (scrollY > document.querySelector('.testimonials').offsetTop + 100) {
        testimonialsVisible.value = true;
      }
      if (scrollY > document.querySelector('.contact').offsetTop + 100) {
        contactVisible.value = true;
      }
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
      handleScroll();
    });

    return {
      heroVisible,
      introVisible,
      servicesVisible,
      testimonialsVisible,
      contactVisible,
      services,
      testimonials,
      bookSession,
      scrollToContent,
    };
  },
};
</script>

<style scoped>
/* Reset and General Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', sans-serif;
  color: #333;
  background-color: #f9f9f9;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: auto;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #6a0572;
  text-align: center;
}

.section-text {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  text-align: center;
  color: #555;
}

button {
  cursor: pointer;
  border: none;
  outline: none;
}

a {
  text-decoration: none;
  color: inherit;
}

/* Hero Section */
.hero {
  position: relative;
  height: 100vh;
  background-image: linear-gradient(135deg, rgba(255, 204, 0, 0.7), rgba(106, 5, 114, 0.7)), url('@/assets/images/hero-background.jpg');
  background-size: cover;
  background-position: center;
  color: white;
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  max-width: 500px;
}

.hero-title {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

.hero-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 1rem 2.5rem;
  border-radius: 50px;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
}

.hero-button:hover {
  background-color: #e65c50;
}

.hero-image-wrapper {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50%;
  height: 100%;
  overflow: hidden;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  cursor: pointer;
}

.scroll-indicator span {
  display: block;
  width: 1rem;
  height: 1rem;
  border-bottom: 2px solid #fff;
  border-right: 2px solid #fff;
  transform: rotate(45deg);
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateX(-50%) rotate(45deg) translateY(0);
  }
  40% {
    transform: translateX(-50%) rotate(45deg) translateY(-15px);
  }
  60% {
    transform: translateX(-50%) rotate(45deg) translateY(-7px);
  }
}

/* Introduction Section */
.introduction {
  padding: 5rem 0;
  background-color: #fff;
}

/* Services Section */
.services {
  padding: 5rem 0;
  background-color: #f8f9fa;
}

.services-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.service-card {
  background-color: #fff;
  padding: 2rem;
  border-radius: 15px;
  width: 300px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.service-icon {
  font-size: 3rem;
  color: #6a0572;
  margin-bottom: 1rem;
}

.service-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.service-description {
  font-size: 1rem;
  color: #777;
}

/* Testimonials Section */
.testimonials {
  padding: 5rem 0;
  background-color: #fff;
}

.testimonials-slider {
  display: flex;
  gap: 2rem;
  overflow-x: auto;
  padding-bottom: 1rem;
  scroll-snap-type: x mandatory;
}

.testimonial-card {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 10px;
  min-width: 300px;
  flex: none;
  scroll-snap-align: start;
  text-align: center;
}

.testimonial-quote {
  font-size: 1.2rem;
  font-style: italic;
  margin-bottom: 1rem;
}

.testimonial-author {
  font-size: 1rem;
  font-weight: bold;
  color: #ff6f61;
}

/* Contact Section */
.contact {
  padding: 5rem 0;
  background-color: #6a0572;
  color: #fff;
  text-align: center;
}

.contact-button {
  background-color: #ffcc00;
  color: #6a0572;
  padding: 1rem 2.5rem;
  border-radius: 50px;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
}

.contact-button:hover {
  background-color: #e6b800;
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

.animate-slide-right {
  animation: slideRight 1s forwards;
}

.animate-zoom-in {
  animation: zoomIn 1s forwards;
}

@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes slideUp {
  0% { opacity: 0; transform: translateY(50px); }
  100% { opacity: 1; transform: translateY(0); }
}

@keyframes slideLeft {
  0% { opacity: 0; transform: translateX(-50px); }
  100% { opacity: 1; transform: translateX(0); }
}

@keyframes slideRight {
  0% { opacity: 0; transform: translateX(50px); }
  100% { opacity: 1; transform: translateX(0); }
}

@keyframes zoomIn {
  0% { opacity: 0; transform: scale(0.8); }
  100% { opacity: 1; transform: scale(1); }
}

/* Media Queries */
@media (max-width: 768px) {
  .hero-content {
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .hero-image-wrapper {
    display: none;
  }

  .service-card, .testimonial-card {
    width: 100%;
  }

  .services-grid, .testimonials-slider {
    flex-direction: column;
    align-items: center;
  }
}
</style>
