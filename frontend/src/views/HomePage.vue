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
    // For example, you can initialize the testimonial slider
  },
};
</script>




<style>
/* Variables */
:root {
  --primary-color: #6a0572;
  --secondary-color: #ff6f61;
  --background-color: #f8f9fa;
  --text-color: #333;
  --light-text-color: #fff;
  --font-family: 'Poppins', sans-serif;
}

/* Keyframe Animations */
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

@keyframes fadeIn {
  to {
    opacity: 1;
  }
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

/* Global Reset (Optional) */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
</style>
