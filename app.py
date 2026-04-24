import streamlit as st
from api_calling import note_generator, audio_transcription, quize_generator
from PIL import Image

# title
st.title("Note Summary and Quiz Generator",anchor=False)
st.markdown("Upload upto 3 images to generate Note summarry and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")

    #work with images
    images= st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)


    if pil_images:
        if len(images)>3:
            st.error("upload at max 3 images")
        
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ('Easy','Medium','Hard'),
        index = None
    )
    # if selected_option:
    #     st.markdown(f"You have selected **{selected_option}** as difficulty")
    # else:
    #     st.error("You must select a difficulty")
    pressed =  st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must selet a difficulty for your quiz")
    
    if images and selected_option:

        #note
        with st.container(border=True):
            st.subheader("Your note", anchor=False)

            #the portion below will be replaced by API call

            #add a spinner
            with st.spinner("AI is writing notes for you"):

                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)





        #Audio Transcrip
        with st.container(border=True):
            st.subheader("Audio Transcription",anchor=False)

            #the portion below will be replaced by API call
            with st.spinner("AI is writing notes for you"):

                # clearing the markdown
                generated_notes =  generated_notes.replace("#","")
                generated_notes =  generated_notes.replace("*","")
                generated_notes =  generated_notes.replace("-","")
                generated_notes =  generated_notes.replace("`","")




                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)




        #Quiz transcript
        with st.container(border=True):
            st.subheader(f"Quiz {selected_option} Difficulty",anchor=False)

            #the portion below will be replaced by API call
            quizzes = quize_generator(pil_images,selected_option)
            st.markdown(quizzes)
