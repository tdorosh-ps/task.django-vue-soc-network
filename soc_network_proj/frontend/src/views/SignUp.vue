<template>
  <div class="container text-center bv-example-row bv-example-row-flex-cols">
    <b-row class="mt-5" align-h="center">
      <b-form class="form" @submit.prevent="signUp">
        <h3>SignUp</h3>
        <b-form-group class="text-left" label="Email" label-for="email">
          <b-form-input
            id="email"
            v-model="email"
            type="email"
            required
          ></b-form-input>
          <b-list-group v-if="emailErrors">
            <b-list-group-item
              v-for="error in emailErrors"
              v-bind:key="error.id"
              variant="danger">
              {{ error }}
            </b-list-group-item>
          </b-list-group>
        </b-form-group>

        <b-form-group class="text-left" label="Password" label-for="password">
          <b-form-input
            id="password"
            v-model="password"
            type="password"
            required
          ></b-form-input>
          <b-list-group v-if="passwordErrors">
            <b-list-group-item
              v-for="error in passwordErrors"
              v-bind:key="error.id"
              variant="danger">
              {{ error }}
            </b-list-group-item>
          </b-list-group>
        </b-form-group>

        <b-form-group class="text-left" label="Confirm Password" label-for="password_repeat">
          <b-form-input
            id="password_repeat"
            v-model="password_repeat"
            type="password"
            required
          ></b-form-input>
          <p v-if="!arePasswordsEqual()" class="alert alert-danger">Passwords must be the same</p>
        </b-form-group>

        <p>Have an account? <b-link :to="{ name: 'signin' }">SignIn</b-link></p>
        <b-button id="submit" type="submit" variant="primary">SignUp</b-button>

      </b-form>
    </b-row>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: "SignUp",
  data() {
    return {
      email: '',
      password: '',
      password_repeat: '',
      emailErrors: '',
      passwordErrors:'',
    }
  },
  methods: {
    signUp() {
      const data = {
        email: this.email,
        password: this.password,
        password_repeat: this.password_repeat
      };
      this.$store.dispatch('createUser', data)
      .then(() => {
        router.push('/signin')
      }, (error) => {
          this.emailErrors = error.response.data.email;
          this.passwordErrors = error.response.data.password;
      })

    },
    arePasswordsEqual() {
      return this.password_repeat === this.password;
    }
  },
}
</script>