<template>
  <transition name="fade">
    <div v-if="showContact" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <button class="close-button" @click="closeModal">&times;</button>
        <h2 class="modal-title">Contact Me</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="name">Your Name</label>
            <input type="text" id="name" v-model="formData.name" required />
          </div>
          <div class="form-group">
            <label for="email">Your Email</label>
            <input type="email" id="email" v-model="formData.email" required />
          </div>
          <div class="form-group">
            <label for="message">Your Message</label>
            <textarea id="message" v-model="formData.message" required></textarea>
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
      // Here you can handle form submission logic, e.g., sending data to your backend
      console.log(this.formData);
      alert('Message sent!');
      this.closeModal(); // Close modal after submission
    },
  },
};
</script>

<style scoped>
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
  font-size: 1rem;
}

textarea {
  resize: none;
  height: 120px;
}

.submit-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 50px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #e65b50;
}
</style>
