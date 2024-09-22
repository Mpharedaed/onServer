<template>
  <transition name="fade">
    <div v-if="showContact" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <button class="close-button" @click="closeModal">&times;</button>
        <h2 class="modal-title">Contact Me</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="name">Your Name</label>
            <input
              type="text"
              id="name"
              v-model="formData.name"
              required
              class="form-input"
            />
          </div>
          <div class="form-group">
            <label for="email">Your Email</label>
            <input
              type="email"
              id="email"
              v-model="formData.email"
              required
              class="form-input"
            />
          </div>
          <div class="form-group">
            <label for="message">Your Message</label>
            <textarea
              id="message"
              v-model="formData.message"
              required
              class="form-input"
            ></textarea>
          </div>
          <button type="submit" class="submit-button">Send Message</button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    showContact: Boolean,
  },
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: '',
      },
    };
  },
  methods: {
    closeModal() {
      this.$emit('close');
      document.body.style.overflow = 'auto';
    },
    submitForm() {
      console.log(this.formData);
      alert('Message sent!');
      this.closeModal();
    },
  },
};
</script>

<style scoped>
/* General Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background-color: #fff;
  padding: 2rem;
  border-radius: 10px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
}

.close-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #333;
}

.close-button:hover {
  color: #ff6f61;
}

.modal-title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #333;
}

input,
textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem; /* Prevent mobile zoom-in */
}

textarea {
  resize: none;
  height: 120px;
}

.submit-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%; /* Full-width button for mobile */
  max-width: 400px;
  margin: 0 auto; /* Center the button */
  display: block;
}

.submit-button:hover {
  background-color: #e65b50;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .modal-content {
    padding: 1.5rem;
    max-width: 90%;
  }

  .modal-title {
    font-size: 1.8rem;
  }

  input,
  textarea {
    font-size: 1rem; /* Prevent zoom on mobile */
  }

  .submit-button {
    padding: 0.75rem 1.5rem;
    font-size: 1.1rem;
  }
}

@media (max-width: 480px) {
  .modal-content {
    padding: 1rem;
    max-width: 95%;
  }

  .modal-title {
    font-size: 1.6rem;
  }

  input,
  textarea {
    font-size: 1rem; /* Ensure no zoom on mobile */
  }

  .submit-button {
    font-size: 1rem;
    padding: 0.75rem 1.5rem;
  }
}

/* Styles for Video Background */
.hero {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.hero video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  filter: brightness(50%);
}

@media (max-width: 768px) {
  .hero video {
    object-fit: contain;
  }
}

</style>

<!-- HTML for the Background Video Section -->

<section class="hero">
  <video autoplay muted loop playsinline>
    <!-- Multiple sources for browser compatibility -->
    <source src="@/assets/video/background.mp4" type="video/mp4" />
    <source src="@/assets/video/background.webm" type="video/webm" />
    <source src="@/assets/video/background.ogv" type="video/ogg" />
    <!-- Fallback image if video doesn't load -->
    <img
      src="@/assets/images/fallback-image.jpg"
      alt="Background Fallback"
      class="fallback-image"
    />
    Your browser does not support the video tag.
  </video>
</section>
