# 3rd HighSchools CTF Workshop - Verona 2023

## Secret sound

We are given an audio file. By listening to it, we can recognize the distinctive sound of pressing keys on a telephone keypad. Specifically, this is _Dual-tone multi-frequency_ (DTMF), a coding system used in telephony to encode numeric codes as audible tone signals.

We can use an online tool such as [DTMF Encoder/Decoder](https://unframework.github.io/dtmf-detect/) to decode the audio signal.  
After decoding, we obtain the following sequence of keys:  
`2331434783711923431767372331117714113`.

By carefully listening to the sound, we notice that the key presses are alternated with moments of silence. The decoded values can therefore be separated as follows:  
`23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13`.

The obtained values share a common feature: they are all prime numbers. Thus, we can map each one to the corresponding letter of the alphabet based on its position in the ordered list of prime numbers.

By doing so, we obtain the flag
```
flag{IKNOWTHINGSLIKEDTMF}
```