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
/* Modal Background */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(20px); /* Frosted glass effect */
  background: rgba(255, 255, 255, 0.2); /* Slight transparency */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

/* Modal Content */
.modal-content {
  background: rgba(255, 255, 255, 0.75); /* Semi-transparent background */
  backdrop-filter: blur(40px); /* Strong blur for the Apple effect */
  padding: 2rem;
  border-radius: 16px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Close Button */
.close-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #333;
  transition: color 0.3s ease;
}
.close-button:hover {
  color: #007aff; /* Apple blue */
}

/* Modal Title */
.modal-title {
  font-size: 1.8rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  color: #000;
  margin-bottom: 1.5rem;
  text-align: center;
}

/* Form Group */
.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #333;
  font-family: inherit;
}

/* Input and Textarea */
input,
textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid rgba(60, 60, 67, 0.15);
  border-radius: 12px;
  font-size: 1rem;
  font-family: inherit;
  background: rgba(255, 255, 255, 0.75);
  outline: none;
  transition: border-color 0.3s ease;
}

textarea {
  resize: none;
  height: 120px;
}

/* Focus States */
input:focus,
textarea:focus {
  border-color: #007aff; /* Apple blue */
}

/* Submit Button */
.submit-button {
  background-color: #007aff;
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 50px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  display: block;
  box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3);
}

.submit-button:hover {
  background-color: #005bb5;
  box-shadow: 0 6px 16px rgba(0, 122, 255, 0.4);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .modal-content {
    padding: 1.5rem;
    max-width: 90%;
  }

  .modal-title {
    font-size: 1.6rem;
  }

  input,
  textarea {
    font-size: 1rem;
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
    font-size: 1.4rem;
  }

  input,
  textarea {
    font-size: 0.9rem;
  }

  .submit-button {
    font-size: 1rem;
    padding: 0.75rem 1.5rem;
  }
}

/* Video Background */
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
