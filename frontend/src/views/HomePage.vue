<template>
  <div class="home">
    <header class="hero-section">
      <div class="content-wrapper">
        <div class="hero-text">
          <h1>Dawlat Emad</h1>
          <p>Your Journey to Self-Discovery and Success Starts Here</p>
          <button class="cta-button">Book a Session</button>
        </div>
        <div class="hero-image-wrapper">
          <img src="@/assets/images/dawlat.png" alt="Dawlat Emad" class="dawlat-image" />
        </div>
      </div>
    </header>

    <main class="main-content">
      <section class="introduction">
        <h2>Welcome to My Coaching Space</h2>
        <p>
          I’m Dawlat Emad, a certified life coach dedicated to helping you
          achieve your personal and professional goals. Together, we can
          navigate the challenges of life, unlock your potential, and build the
          life you’ve always dreamed of.
        </p>
      </section>

      <section class="services">
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
            <p>Custom training programs for organizations aiming to improve team dynamics and leadership skills.</p>
          </div>
        </div>
      </section>

      <section class="testimonials">
        <h2>What My Clients Say</h2>
        <div class="testimonial-cards">
          <div class="testimonial-card">
            <p>"Dawlat helped me find clarity and purpose in my life."</p>
            <h4>- AYA</h4>
          </div>
          <div class="testimonial-card">
            <p>"The best investment I've made in myself. Highly recommend!"</p>
            <h4>- John Doe</h4>
          </div>
          <div class="testimonial-card">
            <p>"Her guidance has been transformative in both my personal and professional life."</p>
            <h4>- Jane Smith</h4>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
/* General Layout */
.home {
  font-family: 'Poppins', sans-serif;
  color: #333;
  background-color: #f8f9fa;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}

/* Hero Section */
.hero-section {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #FFCC00, #6A0572); /* Gradient Background */
  position: relative;
  overflow: hidden;
}

.content-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 90%;
  max-width: 1200px;
}

.hero-text {
  flex: 1;
  max-width: 45%;
  text-align: left;
  color: white;
  z-index: 2;
}

.hero-text h1 {
  font-size: 4em;
  font-weight: 900;
  text-transform: uppercase;
  margin-bottom: 15px;
}

.hero-text p {
  font-size: 1.2em;
  margin-bottom: 30px;
}

.cta-button {
  background-color: #FF6F61;
  color: white;
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

.hero-image-wrapper {
  flex: 1;
  max-width: 45%;
  position: relative;
}

.dawlat-image {
  width: 100%;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

/* Introduction Section */
.introduction {
  padding: 60px 20px;
  text-align: center;
  background-color: #fff;
}

.introduction h2 {
  font-size: 2.5em;
  color: #6a0572;
  margin-bottom: 20px;
}

.introduction p {
  font-size: 1.2em;
  margin: 0 auto;
  max-width: 700px;
  line-height: 1.8;
  color: #555;
}

/* Services Section */
.services {
  padding: 60px 20px;
  text-align: center;
  background-color: #f8f9fa;
}

.services h2 {
  font-size: 2.5em;
  color: #a904b5;
  margin-bottom: 40px;
}

.service-cards {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.service-card {
  background-color: #fff;
  padding: 40px;
  margin: 15px;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  max-width: 280px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}

.service-icon {
  font-size: 2.5em;
  color: #6a0572;
  margin-bottom: 15px;
}

.service-card h3 {
  margin-bottom: 15px;
  font-size: 1.8em;
  color: #333;
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
  padding: 60px 20px;
  text-align: center;
  background-color: #fff;
}

.testimonials h2 {
  font-size: 2.5em;
  color: #a904b5;
  margin-bottom: 40px;
}

.testimonial-cards {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.testimonial-card {
  background-color: #f8f9fa;
  padding: 30px;
  margin: 15px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  max-width: 320px;
  font-style: italic;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}

.testimonial-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.testimonial-card h4 {
  margin-top: 15px;
  font-weight: bold;
  font-size: 1.2em;
  color: #ff6f61;
  text-transform: uppercase;
}
</style>