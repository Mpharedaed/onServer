<template>
  <div v-if="showStory || showQuestionnaire" class="modal-container" @click.self="closeModal">
    <!-- Story Content -->
    <transition name="fade" mode="out-in">
      <div v-if="!showQuestionnaire" class="story-content rtl" key="story">
        <button class="close-button" @click="closeModal">&times;</button>
        <h2 class="story-title">عن دولت عماد</h2>
        <p class="story-text">
          دولت عماد هي كوتش حياة شغوفة، مخصصة إنها تساعد الناس يكتشفوا إمكانياتهم الحقيقية ويحققوا أحلامهم.
          بأسلوب بسيط وجميل بيجمع بين التعاطف والخبرة، دولت بتمكن عملاءها من تجاوز التحديات واكتشاف قوتهم الداخلية.
        </p>
        <h3 class="story-subheading">تخصصات دولت تشمل:</h3>
        <ul class="story-list">
          <li><strong>بناء الثقة:</strong> بتساعد السيدات يستعيدوا قوتهم وصوتهم في الحياة الشخصية والمهنية.</li>
          <li><strong>الكوتشينج المهني:</strong> بترشد الأفراد في تحديد أهدافهم المهنية وتوجيه حياتهم العملية ناحية شغفهم.</li>
          <li><strong>الصحة النفسية:</strong> بتدعم عملاءها في إدارة التوتر والقلق وتعدي المراحل الصعبة في حياتهم بأساليب مخصصة للمرونة النفسية.</li>
          <li><strong>تطوير القيادة:</strong> بتمكن السيدات والقادة الجدد إنهم يمسكوا مناصب قيادية بشجاعة وثقة.</li>
        </ul>
        <p class="story-text">
          دولت معروفة بأسلوبها الدافئ والداعم. بتقدم مش بس أدوات عملية، لكن كمان بتدي الدعم النفسي اللي عملاءها بيحتاجوه عشان يحققوا النجاح.
        </p>
        <button class="story-button" @click="openQuestionnaire">ابدأ رحلتك الآن</button>
      </div>
    </transition>

    <!-- Questionnaire Content -->
    <transition name="slide" mode="out-in">
      <div v-if="showQuestionnaire" class="questionnaire-content rtl" key="questionnaire">
        <button class="close-button" @click="closeModal">&times;</button>
        <transition name="fade" mode="out-in">
          <div :key="currentStep" class="step-content">
            <!-- Progress Bar -->
            <div class="progress-bar">
              <div class="progress" :style="{ width: progressPercentage + '%' }"></div>
            </div>
            <h2 class="question-title">{{ currentQuestion.title }}</h2>
            <div class="question-body">
              <p v-if="currentQuestion.text">{{ currentQuestion.text }}</p>

              <!-- Single Select Options -->
              <div v-if="currentQuestion.type === 'options'" class="options-list">
                <div
                  v-for="(option, index) in currentQuestion.options"
                  :key="index"
                  class="option-item"
                >
                  <input
                    type="radio"
                    :id="`option-${currentStep}-${index}`"
                    :name="`question-${currentStep}`"
                    :value="option"
                    v-model="answers[currentStep]"
                  />
                  <label :for="`option-${currentStep}-${index}`">{{ option }}</label>
                </div>
              </div>

              <!-- Multiple Select (Checkbox) -->
              <div v-if="currentQuestion.type === 'checkbox'" class="checkbox-list">
                <div
                  v-for="(option, index) in currentQuestion.options"
                  :key="index"
                  class="checkbox-option"
                >
                  <input
                    type="checkbox"
                    :id="`checkbox-${currentStep}-${index}`"
                    :value="option"
                    v-model="answers[currentStep]"
                  />
                  <label :for="`checkbox-${currentStep}-${index}`">{{ option }}</label>
                </div>
              </div>

              <!-- Text Input -->
              <div v-if="currentQuestion.type === 'input'">
                <input
                  v-model="answers[currentStep]"
                  :type="currentQuestion.inputType"
                  :placeholder="currentQuestion.placeholder"
                  class="text-input"
                />
              </div>

              <!-- Date Picker -->
              <div v-if="currentQuestion.type === 'date'">
                <input
                  v-model="answers[currentStep]"
                  type="date"
                  class="date-input"
                />
              </div>
            </div>

            <!-- Feedback Message -->
            <p class="feedback-message" v-if="feedbackMessage">{{ feedbackMessage }}</p>

            <!-- Navigation Buttons -->
            <div class="navigation-buttons">
              <button v-if="currentStep > 0" @click="prevStep" class="prev-button">السابق</button>
              <button
                v-if="!isLastStep"
                @click="nextStep"
                class="next-button"
                :disabled="!isStepValid"
              >
                التالي
              </button>
              <button
                v-if="isLastStep"
                @click="submit"
                class="submit-button"
                :disabled="!isStepValid"
              >
                إرسال
              </button>
            </div>
          </div>
        </transition>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'StoryModal',
  props: {
    showStory: Boolean,
  },
  data() {
    return {
      showQuestionnaire: false,
      currentStep: 0,
      answers: {}, // Answer object to store user's responses
      feedbackMessage: '', // For positive feedback messages
      questions: [
        // Introduction
        {
          title: "مرحبًا! تخيل أننا نجلس سويًا مع كوب قهوة (أو شاي). ما هو أول شيء يشغل بالك الآن؟",
          type: "input",
          inputType: "text",
          placeholder: "أخبرني بما يشغل بالك...",
        },
        // Section 1: Identifying the heroes of the story
        {
          title: "كل قصة لها بطل رئيسي. من هو بطل القصة في حياتك الآن؟",
          text: "اختر من يمثل البطل في قصتك.",
          type: "checkbox",
          options: [
            "أنا! أنا بطل قصتي.",
            "عائلتي – هم أساس حياتي.",
            "عملي – كل تركيزي على النجاح المهني.",
            "أصدقائي – هم من يدعمونني دائمًا.",
            "أحلامي – أركض وراءها بكل شغف.",
          ],
        },
        {
          title: "إذا كانت حياتك فيلمًا، ما هو عنوان الفيلم؟",
          type: "input",
          inputType: "text",
          placeholder: "اكتب عنوان الفيلم...",
        },
        // Section 2: Life goals – choose your adventure
        {
          title: "إذا كانت حياتك لعبة فيديو، فما هو المستوى الذي تحاول التغلب عليه الآن؟",
          text: "اختر التحديات التي تعمل على تجاوزها.",
          type: "checkbox",
          options: [
            "تحقيق التوازن بين العمل والحياة",
            "تحسين الصحة النفسية والعاطفية",
            "تسلق سلم النجاح المهني",
            "تحسين العلاقات (العائلة، الأصدقاء، الحياة العاطفية)",
            "تطوير مهارات جديدة",
          ],
        },
        {
          title: "ما هي القوة الخارقة التي تمتلكها للتغلب على التحديات؟",
          text: "اختر قواك الخارقة!",
          type: "checkbox",
          options: [
            "الإصرار – لا أستسلم أبدًا!",
            "الإبداع – أجد حلولًا حتى في أصعب الظروف.",
            "الصبر – أثق أن الخطوات البطيئة تؤدي للنتائج.",
            "حل المشكلات – أرى التحديات كألعاب ألغاز.",
          ],
        },
        {
          title: "كل مغامرة تحتاج إلى شريك. من أو ما هو أكبر نظام دعم لديك؟",
          text: "اختر من يدعمك في رحلتك.",
          type: "checkbox",
          options: [
            "عائلتي",
            "أصدقائي",
            "شريكي العاطفي",
            "نفسي",
            "الكتب، البودكاست، أو المرشدين",
          ],
        },
        // Section 3: The dramatic plot – the challenges you face
        {
          title: "ما هو الانعطاف الحالي في حبكة حياتك؟",
          text: "اختر التحديات التي تواجهها.",
          type: "checkbox",
          options: [
            "أواجه صعوبة في إيجاد الوقت لنفسي.",
            "أشعر بأنني عالق أو بدون دافع.",
            "مستويات التوتر لدي مرتفعة!",
            "أحاول الموازنة بين أشياء كثيرة في وقت واحد.",
            "أشعر بأنني لا أتقدم أو لا أنمو.",
          ],
        },
        {
          title: "إذا كان بإمكانك اختيار أداة سحرية لحل هذا التحدي، ما الذي ستختاره؟",
          text: "اختر أداتك السحرية!",
          type: "checkbox",
          options: [
            "المزيد من الوقت في اليوم",
            "كرة بلورية لتخبرني بالمستقبل",
            "مساعد شخصي ليتولى المهام الصغيرة",
            "مدرب تحفيزي دائم معي",
            "زر 'الهدوء' الفوري للاسترخاء في أي وقت",
          ],
        },
        // Section 4: The dream – drawing your ideal life
        {
          title: "تخيل أنك استيقظت غدًا وكل شيء في حياتك تمامًا كما تريده. ما هو أول شيء ستلاحظه؟",
          text: "اختر ما ستلاحظه أولاً.",
          type: "checkbox",
          options: [
            "أشعر بالهدوء والسعادة والسلام الداخلي.",
            "أعمل في وظيفة أحبها.",
            "علاقاتي تزدهر.",
            "لدي وقت للأشياء التي تجلب لي الفرح.",
            "أعيش في مكان جديد ومثير.",
          ],
        },
        {
          title: "إذا كانت حياتك المثالية مصحوبة بموسيقى تصويرية، ما الأغنية التي ستُعزف في الخلفية؟",
          type: "input",
          inputType: "text",
          placeholder: "اكتب اسم الأغنية...",
        },
        // Section 5: Mental health – checking in on your mind
        {
          title: "على مقياس من 'سيد الهدوء' إلى 'لا أستطيع التحمل'، كيف هي صحتك النفسية هذه الأيام؟",
          text: "اختر الحالة التي تصفك.",
          type: "options",
          options: [
            "سيد الهدوء – أنا هادئ ومسترخي.",
            "الأمور جيدة – لدي أيام جيدة وأخرى سيئة.",
            "أشعر بالتوتر – أحاول السيطرة على الوضع، لكنه صعب.",
            "لا أستطيع التحمل – أواجه صعوبة كبيرة.",
          ],
        },
        {
          title: "ما هو أكثر شيء يسبب لك التوتر؟",
          text: "اختر ما يسبب لك التوتر.",
          type: "checkbox",
          options: [
            "ضغط العمل أو المواعيد النهائية",
            "المسؤوليات العائلية",
            "الضغط المالي",
            "قلة الوقت لنفسي",
            "الشعور بالعزلة عن الآخرين",
          ],
        },
        // Section 6: Your superpower – exploring your strengths
        {
          title: "ما هي الموهبة المخفية التي حتى أصدقاؤك المقربون قد لا يعرفونها؟",
          text: "اختر مواهبك المخفية.",
          type: "checkbox",
          options: [
            "لدي قدرة مذهلة على الحفاظ على الهدوء تحت الضغط.",
            "أنا ماهر في القيام بعدة مهام في وقت واحد.",
            "أستمع باهتمام شديد وأفهم الآخرين.",
            "لدي قدرة إبداعية على حل المشكلات.",
            "عندما أضع هدفًا، ألتزم به بقوة كبيرة.",
          ],
        },
        // Section 7: Personal values – what drives you?
        {
          title: "عندما تتخذ قرارًا، ما هو الشيء الأساسي الذي تأخذه في الاعتبار؟",
          text: "اختر أهم ما تفكر به.",
          type: "options",
          options: [
            "كيف سيؤثر ذلك على مستقبلي",
            "كيف سيؤثر ذلك على علاقاتي",
            "كيف يتماشى مع نموي الشخصي",
            "كيف سيجعلني أشعر في اللحظة الحالية",
          ],
        },
        {
          title: "ما هي القيمة أو المعتقد الذي لا تتنازل عنه أبدًا؟",
          type: "input",
          inputType: "text",
          placeholder: "اكتب قيمتك...",
        },
        // Section 8: Vision of the future – the conclusion of your story
        {
          title: "تخيل أنك تنظر إلى حياتك بعد 10 سنوات من الآن. ما هو الشيء الوحيد الذي تأمل أنك قد حققته بحلول ذلك الوقت؟",
          type: "input",
          inputType: "text",
          placeholder: "اكتب طموحك...",
        },
        {
          title: "ما هي أول خطوة يمكنك اتخاذها اليوم للبدء في تحقيق هذا المستقبل؟",
          type: "input",
          inputType: "text",
          placeholder: "اكتب خطوتك الأولى...",
        },
        // Closing question
        {
          title: "قبل أن ننتهي، هل هناك أي شيء آخر تود مشاركته؟",
          type: "input",
          inputType: "text",
          placeholder: "مساحتك للتعبير الحر...",
        },
        // Contact info
        {
          title: "شكراً لمشاركتك! من فضلك أدخل بريدك الإلكتروني للتواصل.",
          type: "input",
          inputType: "email",
          placeholder: "example@example.com",
        },
        {
          title: "وأخيراً، ما هو رقم هاتفك؟",
          type: "input",
          inputType: "tel",
          placeholder: "رقم الهاتف",
        },
      ],
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentStep];
    },
    isLastStep() {
      return this.currentStep === this.questions.length - 1;
    },
    isStepValid() {
      const answer = this.answers[this.currentStep];
      const question = this.currentQuestion;

      if (question.type === 'input') {
        if (question.inputType === 'email') {
          return !!answer && this.validateEmail(answer);
        } else if (question.inputType === 'tel') {
          return !!answer && this.validatePhoneNumber(answer);
        } else {
          return !!answer && answer.trim().length > 0;
        }
      } else if (question.type === 'date') {
        return !!answer;
      } else if (question.type === 'checkbox') {
        return Array.isArray(answer) && answer.length > 0;
      } else if (question.type === 'options') {
        return !!answer;
      }
      return false;
    },
    progressPercentage() {
      return Math.round(((this.currentStep + 1) / this.questions.length) * 100);
    },
  },
  methods: {
    initializeAnswer(step) {
      const question = this.questions[step];
      if (this.answers[step] === undefined) {
        if (question.type === 'checkbox') {
          this.$set(this.answers, step, []); // Initialize as an array for checkboxes
        } else {
          this.$set(this.answers, step, ''); // Initialize as a string for other input types
        }
      }
    },
    closeModal() {
      this.$emit('close');
      this.showQuestionnaire = false;
      this.currentStep = 0;
      this.answers = {};
      this.feedbackMessage = '';
      document.body.style.overflow = 'auto';
    },
    openQuestionnaire() {
      this.showQuestionnaire = true;
      this.currentStep = 0;
      this.answers = {};
      this.feedbackMessage = '';
      this.initializeAnswer(this.currentStep);
    },
    nextStep() {
      if (this.isStepValid) {
        this.provideFeedback();
        if (this.currentStep < this.questions.length - 1) {
          setTimeout(() => {
            this.currentStep++;
            this.initializeAnswer(this.currentStep);
            this.feedbackMessage = '';
          }, 500);
        }
      }
    },
    prevStep() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.feedbackMessage = '';
      }
    },
    submit() {
      if (this.isStepValid) {
        const userData = {
          answers: this.answers,
          email: this.answers[this.questions.length - 2], // Assuming email is the second last question
          phone: this.answers[this.questions.length - 1], // Assuming phone is the last question
        };
        console.log('User Data:', userData);
        // Here you can send the data to your server or perform any action you need.
        this.closeModal();
      }
    },
    validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    },
    validatePhoneNumber(phone) {
      const re = /^\+?\d{10,15}$/;
      return re.test(phone);
    },
    provideFeedback() {
      const feedbackOptions = [
        'اختيار رائع!',
        'إجابة مميزة!',
        'أحسنت!',
        'ممتاز، استمر!',
        'إجاباتك رائعة!',
      ];
      this.feedbackMessage =
        feedbackOptions[Math.floor(Math.random() * feedbackOptions.length)];
    },
  },
  mounted() {
    this.initializeAnswer(this.currentStep); // Initialize answers on mount
  },
  watch: {
    currentStep(newStep) {
      this.initializeAnswer(newStep); // Ensure answer object is initialized for new steps
    },
  },
};
</script>

<style scoped>
/* General Modal Styles */
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(30, 30, 30, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

/* Story and Questionnaire Content */
.story-content,
.questionnaire-content {
  background: #fff;
  width: 90%;
  max-width: 800px;
  padding: 2rem 3rem;
  border-radius: 20px;
  position: relative;
  animation: fadeInUp 0.5s ease-in-out;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  max-height: 90vh;
  overflow-y: auto;
}

/* Close Button */
.close-button {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: none;
  border: none;
  font-size: 2rem;
  color: #999;
  cursor: pointer;
  z-index: 1100;
  transition: color 0.3s ease;
}
.close-button:hover {
  color: #333;
}

/* Progress Bar */
.progress-bar {
  width: 100%;
  background-color: #e0e0e0;
  height: 10px;
  border-radius: 5px;
  margin-bottom: 1rem;
  overflow: hidden;
}
.progress {
  height: 100%;
  background-color: #ff6f61;
  transition: width 0.3s ease;
}

/* Titles */
.story-title,
.question-title {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-family: 'Cairo', sans-serif;
  font-weight: 700;
  color: #333;
  text-align: center;
}

/* Text */
.story-text,
.question-body p {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 1.5rem;
  font-family: 'Cairo', sans-serif;
  text-align: center;
}

/* Story List */
.story-list {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
}

.story-list li {
  font-size: 1.2rem;
  line-height: 1.8;
  margin-bottom: 1rem;
  position: relative;
  padding-right: 1.5rem;
  font-family: 'Cairo', sans-serif;
  color: #333;
}
.story-list li::before {
  content: '✔';
  position: absolute;
  right: 0;
  color: #ff6f61;
  font-size: 1.5rem;
}

/* Story Button */
.story-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 0.8rem 2rem;
  border-radius: 30px;
  font-size: 1rem;
  transition: background-color 0.3s ease;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
  margin: 0 auto;
  display: block;
}
.story-button:hover {
  background-color: #e65b50;
}

/* Questionnaire Styles */
.option-item,
.checkbox-option {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  width: 100%;
  max-width: 400px;
}

.option-item input[type='radio'],
.checkbox-option input[type='checkbox'] {
  accent-color: #ff6f61;
  margin-left: 1rem;
  transform: scale(1.2);
}

.option-item label,
.checkbox-option label {
  font-size: 1.2rem;
  color: #333;
  font-family: 'Cairo', sans-serif;
  flex: 1;
  text-align: right;
}

.text-input,
.date-input {
  width: 100%;
  max-width: 400px;
  padding: 0.7rem 1rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 30px;
  outline: none;
  text-align: center;
  margin: 0 auto 1rem;
  display: block;
}

/* Feedback Message */
.feedback-message {
  font-size: 1.2rem;
  color: #28a745;
  margin-top: 1rem;
  text-align: center;
  animation: fadeIn 0.5s ease-in-out;
}

/* Navigation Buttons */
.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
}

.prev-button,
.next-button,
.submit-button {
  background-color: #ff6f61;
  color: #fff;
  padding: 0.7rem 1.5rem;
  border: none;
  border-radius: 30px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.prev-button:hover,
.next-button:hover,
.submit-button:hover {
  background-color: #e65b50;
}
.prev-button:disabled,
.next-button:disabled,
.submit-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translate3d(0, 20px, 0);
  }
  to {
    opacity: 1;
    transform: translateZ(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s ease;
}
.slide-enter,
.slide-leave-to {
  transform: translateY(100%);
  opacity: 0;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .story-content,
  .questionnaire-content {
    padding: 1rem;
    max-width: 100%;
    border-radius: 10px;
  }

  .story-title,
  .question-title {
    font-size: 2rem;
  }

  .option-item label,
  .checkbox-option label {
    font-size: 1rem;
  }

  .text-input,
  .date-input {
    font-size: 0.9rem;
    padding: 0.6rem 1rem;
  }

  .navigation-buttons button {
    font-size: 0.9rem;
    padding: 0.6rem 1.2rem;
  }

  .close-button {
    font-size: 1.5rem;
    padding: 8px;
  }
}

@media (max-width: 480px) {
  .story-title,
  .question-title {
    font-size: 1.8rem;
  }

  .option-item label,
  .checkbox-option label {
    font-size: 0.9rem;
  }

  .text-input,
  .date-input {
    font-size: 0.8rem;
    padding: 0.5rem 0.8rem;
  }

  .navigation-buttons button {
    font-size: 0.8rem;
    padding: 0.5rem 1rem;
  }

  .close-button {
    font-size: 1.3rem;
    padding: 6px;
  }
}
</style>
