<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="7">
        <v-text-field
          label="検索したい言葉を入力してください"
          v-model="searchWord"
        ></v-text-field>
      </v-col>
      <v-col cols="3">
        <v-select
          v-model="searchLang"
          :hint="`lang:${searchLang.value}`"
          :items="searchLangItems"
          item-text="lang"
          item-value="value"
          label="Select"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <v-btn
          block
          outlined
          color="cyan"
          @click.native="searchTweets"
        >
          検索
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TwitterSearchBar',

  data: () => ({
    searchWord: '',
    searchLang: { lang: '英語', value: 'en' },
    searchLangItems: [
      { lang: '日本語', value: 'ja' },
      { lang: '英語', value: 'en' }
    ]
  }),

  methods: {
    /**
     * 検索
     */
    searchTweets: function () {
      this.$emit('toggle-searching', true)

      const sendData = {
        searchWord: this.searchWord,
        searchLang: this.searchLang.value
      }

      axios
        .post('/api/search', sendData)
        .then((response) => {
          this.$emit('update-tweet-list', response.data)
          this.$emit('toggle-searching', false)
        })
        .catch((err) => {
          alert('APIサーバの接続に失敗しました')
          this.$emit('update-tweet-list', [])
          this.$emit('toggle-searching', false)
          err = null
        })
    }
  }
}
</script>
