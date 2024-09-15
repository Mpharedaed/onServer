<template>
  <div class="home">
    <!-- Hero Section -->
    <header class="hero-section">
      <div class="overlay"></div>
      <div class="content-wrapper">
        <!-- Navigation Bar -->
        <nav class="navbar">
          <div class="logo">Dawlat Emad</div>
          <ul class="nav-links">
            <li><a href="#services">Services</a></li>
            <li><a href="#testimonials">Testimonials</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
        <!-- Hero Content -->
        <div class="hero-content">
          <h1 class="fade-in">Discover Your Potential</h1>
          <p class="fade-in-delay">
            Empowering you to achieve greatness through personalized coaching.
          </p>
          <button class="cta-button pulse-button">Book a Session</button>
        </div>
        <!-- Scroll Indicator -->
        <div class="scroll-indicator">
          <span></span>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Introduction Section -->
      <section class="introduction">
        <div class="container">
          <h2>Welcome to My Coaching Space</h2>
          <p>
            I’m <strong>Dawlat Emad</strong>, a certified life coach dedicated to helping you
            achieve your personal and professional goals. Together, we can
            navigate the challenges of life, unlock your potential, and build the
            life you’ve always dreamed of.
          </p>
        </div>
      </section>

      <!-- Services Section -->
      <section class="services" id="services">
        <div class="container">
          <h2>Services I Offer</h2>
          <div class="service-cards">
            <div class="service-card">
              <i class="fas fa-user-circle service-icon"></i>
              <h3>Personal Coaching</h3>
              <p>One-on-one sessions tailored to your unique needs and goals.</p>
            </div>
            <div class="service-card">
              <i class="fas fa-users service-icon"></i>
              <h3>Group Workshops</h3>
              <p>Engaging group sessions to foster community and shared learning.</p>
            </div>
            <div class="service-card">
              <i class="fas fa-building service-icon"></i>
              <h3>Corporate Training</h3>
              <p>
                Custom training programs for organizations aiming to improve team dynamics and leadership skills.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Testimonials Section -->
      <section class="testimonials" id="testimonials">
        <div class="container">
          <h2>What My Clients Say</h2>
          <div class="testimonial-slider">
            <div class="testimonial-slide active">
              <p>"Dawlat helped me find clarity and purpose in my life."</p>
              <h4>- Aya</h4>
            </div>
            <div class="testimonial-slide">
              <p>"The best investment I've made in myself. Highly recommend!"</p>
              <h4>- John Doe</h4>
            </div>
            <div class="testimonial-slide">
              <p>
                "Her guidance has been transformative in both my personal and professional life."
              </p>
              <h4>- Jane Smith</h4>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section class="contact" id="contact">
        <div class="container">
          <h2>Get in Touch</h2>
          <p>Ready to start your journey? Contact me today!</p>
          <button class="cta-button">Contact Me</button>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; 2023 Dawlat Emad Coaching. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>



<script>
export default {
  name: "HomePage",
  mounted() {
    // Initialize any JavaScript plugins or components here
  },
};
</script>


<style scoped>
/* Variables */
:root {
  --primary-color: #6a0572;
  --secondary-color: #ff6f61;
  --background-color: #f8f9fa;
  --text-color: #333;
  --light-text-color: #fff;
  --font-family: 'Poppins', sans-serif;
}

/* Global Styles */
.home {
  font-family: var(--font-family);
  color: var(--text-color);
  background-color: var(--background-color);
  margin: 0;
  padding: 0;
  line-height: 1.6;
}

/* Navbar */
.navbar {
  position: absolute;
  top: 0;
  width: 100%;
  padding: 20px 50px;
  display: flex;
  justify-content: space-between;
  z-index: 10;
}

.logo {
  color: var(--light-text-color);
  font-size: 1.8em;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li {
  margin-left: 30px;
}

.nav-links a {
  color: var(--light-text-color);
  text-decoration: none;
  font-size: 1.1em;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: var(--secondary-color);
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 100vh;
  background-image: url("@/assets/images/hero-background.jpg");
  background-size: cover;
  background-position: center;
  overflow: hidden;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.content-wrapper {
  position: relative;
  z-index: 2;
  height: 100%;
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: var(--light-text-color);
}

.hero-content h1 {
  font-size: 4em;
  font-weight: 900;
  text-transform: uppercase;
  margin-bottom: 15px;
}

.hero-content p {
  font-size: 1.5em;
  margin-bottom: 30px;
}

.cta-button {
  background-color: var(--secondary-color);
  color: var(--light-text-color);
  padding: 15px 40px;
  border: none;
  border-radius: 50px;
  font-size: 1.2em;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
  box-shadow: 0 8px 15px rgba(255, 111, 97, 0.4);
}

.cta-button:hover {
  background-color: #ff4a3d;
  transform: scale(1.05);
}

.pulse-button {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 111, 97, 0.7);
  }
  70% {
    box-shadow: 0 0 0 20px rgba(255, 111, 97, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 111, 97, 0);
  }
}

/* Scroll Indicator */
.scroll-indicator {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.scroll-indicator span {
  display: block;
  width: 2px;
  height: 50px;
  background-color: var(--light-text-color);
  animation: scroll 2s infinite;
}

@keyframes scroll {
  0% {
    opacity: 0;
    transform: translateY(0);
  }
  50% {
    opacity: 1;
    transform: translateY(15px);
  }
  100% {
    opacity: 0;
    transform: translateY(30px);
  }
}

/* Fade-in Animations */
.fade-in {
  opacity: 0;
  animation: fadeIn 1s forwards;
}

.fade-in-delay {
  opacity: 0;
  animation: fadeIn 1s forwards 0.5s;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

/* Introduction Section */
.introduction {
  padding: 100px 20px;
  text-align: center;
  background-color: #fff;
}

.introduction .container {
  max-width: 800px;
  margin: 0 auto;
}

.introduction h2 {
  font-size: 2.8em;
  color: var(--primary-color);
  margin-bottom: 30px;
}

.introduction p {
  font-size: 1.2em;
  line-height: 1.8;
  color: #555;
}

/* Services Section */
.services {
  padding: 100px 20px;
  background-color: var(--background-color);
}

.services .container {
  max-width: 1200px;
  margin: 0 auto;
}

.services h2 {
  font-size: 2.8em;
  color: var(--primary-color);
  text-align: center;
  margin-bottom: 60px;
}

.service-cards {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.service-card {
  background-color: #fff;
  padding: 40px;
  margin: 15px;
  border-radius: 15px;
  flex: 1;
  min-width: 280px;
  max-width: 360px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}

.service-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 5px;
  background: linear-gradient(90deg, transparent, var(--secondary-color), transparent);
  animation: borderSlide 3s infinite;
}

@keyframes borderSlide {
  0% {
    left: -100%;
  }
  50% {
    left: 100%;
  }
  100% {
    left: 100%;
  }
}

.service-icon {
  font-size: 3em;
  color: var(--primary-color);
  margin-bottom: 20px;
}

.service-card h3 {
  margin-bottom: 15px;
  font-size: 1.8em;
  color: var(--text-color);
}

.service-card p {
  font-size: 1.1em;
  color: #777;
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

/* Testimonials Section */
.testimonials {
  padding: 100px 20px;
  background-color: #fff;
}

.testimonials .container {
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}

.testimonials h2 {
  font-size: 2.8em;
  color: var(--primary-color);
  margin-bottom: 60px;
}

.testimonial-slider {
  position: relative;
  overflow: hidden;
}

.testimonial-slide {
  opacity: 0;
  position: absolute;
  left: 0;
  width: 100%;
  transition: opacity 1s ease-in-out;
}

.testimonial-slide.active {
  opacity: 1;
  position: relative;
}

.testimonial-slide p {
  font-size: 1.5em;
  font-style: italic;
  color: #555;
  margin-bottom: 20px;
}

.testimonial-slide h4 {
  font-size: 1.2em;
  font-weight: bold;
  color: var(--secondary-color);
}

/* Contact Section */
.contact {
  padding: 100px 20px;
  background-color: var(--background-color);
  text-align: center;
}

.contact .container {
  max-width: 800px;
  margin: 0 auto;
}

.contact h2 {
  font-size: 2.8em;
  color: var(--primary-color);
  margin-bottom: 30px;
}

.contact p {
  font-size: 1.2em;
  color: #555;
  margin-bottom: 40px;
}

.contact .cta-button {
  padding: 15px 50px;
}

/* Footer */
.footer {
  background-color: var(--primary-color);
  color: var(--light-text-color);
  padding: 20px 0;
  text-align: center;
}

.footer p {
  margin: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .service-cards {
    flex-direction: column;
    align-items: center;
  }

  .navbar {
    flex-direction: column;
    align-items: center;
  }

  .nav-links {
    flex-direction: column;
    margin-top: 10px;
  }

  .nav-links li {
    margin: 10px 0;
  }

  .hero-content h1 {
    font-size: 2.5em;
  }

  .hero-content p {
    font-size: 1.2em;
  }
}
</style>

