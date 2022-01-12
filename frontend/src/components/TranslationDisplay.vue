<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="translateLang"
          :items="translateLangItems"
          item-text="lang"
          item-value="value"
          label="Select"
          prepend-icon="mdi-translate"
          return-object
          single-line
        ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-card
          :loading="isTranslating"
        >
          <v-card-text>
            {{ translatedData.text }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'TranslationDisplay',

  props: {
    isTranslating: Boolean,
    translatedData: Object
  },

  data: () => ({
    translateLang: { lang: '日本語', value: 'JA' },
    translateLangItems: [
      { lang: '日本語', value: 'JA' },
      { lang: '英語', value: 'EN-US' }
    ]
  }),

  watch: {
    translateLang: function (translateLang) {
      this.$emit('update-translate-lang-value', translateLang.value)
    }
  }
}
</script>
