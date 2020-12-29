<template>
  <div class="container text-center bv-example-row bv-example-row-flex-cols">
    <b-row class="mt-5" align-h="center">
      <b-alert
        variant="success"
        :show="isUserCreated"
        dismissible>
        New user was created successfully.
        Now you can sign in with your email and password.
      </b-alert>
    </b-row>
    <b-row class="mt-5" align-h="center">
      <b-form @submit.prevent="signIn">
        <h3>SignIn</h3>
        <b-alert :show="isError" variant="warning" dismissible>Authentication error</b-alert>
        <b-form-group class="text-left" label="Email" label-for="email">
          <b-form-input
            id="email"
            v-model="email"
            type="text"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group class="text-left" label="Password" label-for="password">
          <b-form-input
            id="password"
            v-model="password"
            type="password"
            required
          ></b-form-input>
        </b-form-group>
        <p>Do not have an account? <b-link :to="{ name: 'signup' }">SignUp</b-link></p>
        <b-button id="submit" type="submit" variant="primary">SignIn</b-button>
      </b-form>
    </b-row>
  </div>
</template>

<script>

export default {
  name: "SignIn",
  data() {
    return {
      email: '',
      password: ''
    }
  },
  computed: {
    isError() {
      return this.$store.getters.authStatus === 'error';
    },
    isUserCreated() {
      return this.$store.getters.userEvent === 'create';
    },
  },
  methods: {
    signIn() {
      const { email, password } = this;
      this.$store.dispatch('authRequest', { email, password })
      .then(() => {
        this.$router.push('/posts/own');
        this.$store.dispatch('getUser');
      });
    }
  }
}
</script>