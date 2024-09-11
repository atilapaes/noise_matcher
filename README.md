# noise_matcher
 Record, detect, identify and characterize noise sources
 
 Feature description:
 
**rec**: Record audio with default or personalized parameters.

**signal_detector**: Process the recorded audio using different techniques and detectec signals.

**signal_extractor**: Use the information created by the signal detector and extract the samples of audio that contains the signal.

**signal_characterizer**: Characterize the signals extracted using different techniques.

**manual_classifier**: Read input from users and tags signal samples.

**auto_classifier**: Compare characterization of new signals with the tags provided by the user, create metrics for the best matches, and rank then based in the scores.
