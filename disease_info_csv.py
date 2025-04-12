import csv

# Create a comprehensive disease information dictionary
disease_info = {
    'Apple__Apple_scab': {
        'symptoms': "Brown or olive-green spots on leaves and fruit, eventually turning dark and scabby. Infected leaves may twist, pucker, or fall early.",
        'causes': "Fungal pathogen Venturia inaequalis, thrives in cool, wet spring weather.",
        'solution': "Apply fungicides like Captan or Mancozeb and remove infected leaves.",
        'prevention': "Plant resistant varieties, rake and destroy fallen leaves, ensure good air circulation with proper pruning."
    },
    'Apple__Black_rot': {
        'symptoms': "Purple spots on leaves, rotting fruit with concentric rings, and cankers on branches.",
        'causes': "Fungus Botryosphaeria obtusa, favors warm, humid conditions.",
        'solution': "Use copper-based fungicides and ensure proper spacing for air circulation.",
        'prevention': "Prune out dead or diseased wood, remove mummified fruit, maintain tree vigor with proper fertilization."
    },
    'Apple__Cedar_apple_rust': {
        'symptoms': "Bright orange-yellow spots on leaves and fruit, sometimes with small black dots in the center.",
        'causes': "Fungus Gymnosporangium juniperi-virginianae, requires both apple trees and junipers to complete lifecycle.",
        'solution': "Apply fungicides such as myclobutanil, and remove infected leaves.",
        'prevention': "Remove nearby juniper or cedar trees if possible, plant resistant varieties."
    },
    'Apple__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Maintain proper care and monitoring, no disease detected.",
        'prevention': "Regular pruning, appropriate fertilization, consistent watering, and preventive fungicide program."
    },
    'Blueberry__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Ensure proper irrigation, prune any dead or damaged branches.",
        'prevention': "Maintain soil pH between 4.5-5.5, mulch with pine needles or acidic compost, adequate spacing between plants."
    },
    'Cherry_(including_sour)__Powdery_mildew': {
        'symptoms': "White powdery substance on leaves, shoots, and sometimes fruit, causing leaf curling and stunted growth.",
        'causes': "Fungus Podosphaera clandestina, favors high humidity with moderate temperatures.",
        'solution': "Apply sulfur-based fungicides and prune affected branches.",
        'prevention': "Ensure good air circulation, avoid overhead irrigation, plant resistant varieties."
    },
    'Cherry_(including_sour)__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Regularly inspect for pests and diseases and prune dead branches.",
        'prevention': "Maintain proper pruning, adequate spacing, appropriate fertilization, and irrigation."
    },
    'Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot': {
        'symptoms': "Small, rectangular lesions that are tan to gray with yellow halos, eventually merging to create large necrotic areas.",
        'causes': "Fungus Cercospora zeae-maydis, thrives in humid conditions with heavy dew.",
        'solution': "Apply fungicides like Chlorothalonil and avoid excessive irrigation.",
        'prevention': "Crop rotation, tillage to bury crop residue, plant resistant hybrids, improve field drainage."
    },
    'Corn_(maize)__Common_rust_': {
        'symptoms': "Small, round to elongate brown to reddish-brown pustules on both leaf surfaces, husks, and tassels.",
        'causes': "Fungus Puccinia sorghi, favors cool temperatures (60-77°F) and high humidity.",
        'solution': "Apply rust-resistant corn varieties and use fungicides like Azoxystrobin.",
        'prevention': "Plant resistant hybrids, early planting to avoid optimal rust conditions, eliminate alternate hosts."
    },
    'Corn_(maize)__Northern_Leaf_Blight': {
        'symptoms': "Long, elliptical, grayish-green to tan lesions that develop on leaves, can lead to significant leaf loss.",
        'causes': "Fungus Exserohilum turcicum, favors moist conditions with moderate temperatures.",
        'solution': "Use resistant varieties and apply fungicides like Chlorothalonil.",
        'prevention': "Crop rotation, tillage to bury crop residue, plant resistant hybrids, optimal plant spacing."
    },
    'Corn_(maize)__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy tassel and ear development.",
        'causes': "N/A",
        'solution': "Ensure proper irrigation and pest control practices.",
        'prevention': "Crop rotation, balanced fertilization, proper plant spacing, regular monitoring."
    },
    'Grape__Black_rot': {
        'symptoms': "Small, dark spots on leaves that enlarge and develop tan centers with black borders. Fruit shrivels into black, hard 'mummies'.",
        'causes': "Fungus Guignardia bidwellii, favors warm, humid conditions.",
        'solution': "Apply fungicides like Mancozeb and prune affected parts.",
        'prevention': "Remove mummified berries and infected leaves, ensure proper canopy management for air circulation."
    },
    'Grape__Esca_(Black_Measles)': {
        'symptoms': "Red-brown spots between leaf veins that merge to form stripes, fruit with purple spotting.",
        'causes': "Complex of fungi including Phaeomoniella chlamydospora and Phaeoacremonium species, enters through pruning wounds.",
        'solution': "Remove and destroy infected vines, and apply fungicides.",
        'prevention': "Prune during dry weather, seal large pruning cuts, avoid stress to vines."
    },
    'Grape__Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'symptoms': "Small, reddish spots with dark borders that enlarge and cause tissue death, leaves may drop prematurely.",
        'causes': "Fungus Pseudocercospora vitis (formerly Isariopsis leaf spot), thrives in warm, wet conditions.",
        'solution': "Apply fungicides like Chlorothalonil and avoid overhead irrigation.",
        'prevention': "Remove fallen leaves, improve air circulation through proper pruning, maintain proper vine nutrition."
    },
    'Grape__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Maintain proper care and monitor for pests regularly.",
        'prevention': "Regular pruning for good air circulation, balanced fertilization, adequate spacing between vines."
    },
    'Orange__Haunglongbing_(Citrus_greening)': {
        'symptoms': "Yellow mottling of leaves not following vein patterns, lopsided bitter fruit, twig dieback.",
        'causes': "Bacteria Candidatus Liberibacter spread by Asian citrus psyllid insect.",
        'solution': "No cure available; remove and destroy infected trees to prevent spread.",
        'prevention': "Control psyllid populations with insecticides, plant disease-free stock, inspect regularly."
    },
    'Peach__Bacterial_spot': {
        'symptoms': "Small water-soaked lesions on leaves that turn purple-brown, fruit with deep pits and cracks.",
        'causes': "Bacteria Xanthomonas arboricola pv. pruni, spreads in warm, wet conditions.",
        'solution': "Apply copper-based bactericides and ensure good air circulation.",
        'prevention': "Plant resistant varieties, avoid overhead irrigation, maintain proper tree nutrition."
    },
    'Peach__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Maintain regular pruning and fertilization for strong growth.",
        'prevention': "Regular pruning, balanced fertilization, proper irrigation, pest monitoring."
    },
    'Pepper_bell__Bacterial_spot': {
        'symptoms': "Small water-soaked spots on leaves and fruit that enlarge and turn brown with yellow halos.",
        'causes': "Bacteria Xanthomonas campestris pv. vesicatoria, spreads by wind, rain, and handling.",
        'solution': "Apply copper-based sprays and rotate crops to prevent recurrence.",
        'prevention': "Use disease-free seeds, avoid overhead watering, practice crop rotation."
    },
    'Pepper_bell__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Ensure consistent watering and proper spacing between plants.",
        'prevention': "Proper spacing, consistent irrigation, balanced fertilization, regular monitoring for pests."
    },
    'Potato__Early_blight': {
        'symptoms': "Dark brown to black concentric rings forming target-like patterns on lower leaves first.",
        'causes': "Fungus Alternaria solani, favors warm, wet conditions.",
        'solution': "Apply fungicides and practice crop rotation with non-host plants.",
        'prevention': "Mulch around plants, avoid overhead irrigation, ensure adequate plant spacing."
    },
    'Potato__Late_blight': {
        'symptoms': "Water-soaked pale to dark green spots on leaves that quickly enlarge to become brown-black and oily-looking.",
        'causes': "Oomycete Phytophthora infestans, favors cool, moist conditions.",
        'solution': "Apply fungicides containing chlorothalonil or mancozeb as preventive measure.",
        'prevention': "Plant resistant varieties, destroy volunteer potatoes, eliminate cull piles, improve air circulation."
    },
    'Potato__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy tuber development.",
        'causes': "N/A",
        'solution': "Maintain proper hilling and avoid overhead irrigation.",
        'prevention': "Crop rotation, plant certified seed potatoes, proper hilling, adequate spacing."
    },
    'Raspberry__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Prune canes regularly and maintain proper plant spacing.",
        'prevention': "Remove spent floricanes after harvest, ensure good air circulation, avoid overhead irrigation."
    },
    'Soybean__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy pod development.",
        'causes': "N/A",
        'solution': "Practice crop rotation and maintain optimal soil pH.",
        'prevention': "Rotate with non-host crops, ensure proper drainage, use disease-free seeds."
    },
    'Squash__Powdery_mildew': {
        'symptoms': "White powdery spots on leaves and stems that enlarge to cover entire surfaces.",
        'causes': "Fungi of the Erysiphaceae family, favors dry conditions with high humidity.",
        'solution': "Apply sulfur-based fungicides and ensure proper air circulation.",
        'prevention': "Plant resistant varieties, ensure proper spacing, avoid overhead irrigation."
    },
    'Strawberry__Leaf_scorch': {
        'symptoms': "Small purple spots on leaves that enlarge and develop red-purple borders with tan to gray centers.",
        'causes': "Fungus Diplocarpon earlianum, spreads during warm, wet conditions.",
        'solution': "Remove infected leaves and apply fungicides like captan or copper-based products.",
        'prevention': "Use disease-free plants, ensure good air circulation, avoid overhead irrigation."
    },
    'Strawberry__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Maintain proper irrigation and remove runners as needed.",
        'prevention': "Plant in well-drained soil, use mulch, practice crop rotation, remove runners to prevent overcrowding."
    },
    'Tomato__Bacterial_spot': {
        'symptoms': "Small water-soaked spots on leaves, stems and fruit that enlarge and turn dark brown to black.",
        'causes': "Bacteria Xanthomonas campestris pv. vesicatoria, spreads in warm, wet conditions.",
        'solution': "Apply copper-based bactericides and remove infected plant material.",
        'prevention': "Use disease-free seeds, avoid overhead watering, rotate crops, maintain proper spacing."
    },
    'Tomato__Early_blight': {
        'symptoms': "Dark brown spots with concentric rings forming a target-like pattern on lower leaves first.",
        'causes': "Fungus Alternaria solani, favors warm, humid conditions.",
        'solution': "Apply fungicides containing chlorothalonil or copper and remove lower infected leaves.",
        'prevention': "Mulch around plants, stake or cage plants for better air circulation, avoid overhead irrigation."
    },
    'Tomato__Late_blight': {
        'symptoms': "Water-soaked gray-green spots on leaves that quickly turn brown-black, white fuzzy growth on undersides in moist conditions.",
        'causes': "Oomycete Phytophthora infestans, favors cool, wet conditions.",
        'solution': "Apply fungicides preventively and remove infected plants entirely to prevent spread.",
        'prevention': "Improve air circulation, avoid overhead irrigation, plant resistant varieties, rotate crops."
    },
    'Tomato__Leaf_Mold': {
        'symptoms': "Yellow spots on upper leaf surfaces with olive-green to gray fuzzy growth on undersides.",
        'causes': "Fungus Passalora fulva (formerly Fulvia fulva), favors high humidity and moderate temperatures.",
        'solution': "Improve air circulation and apply fungicides containing chlorothalonil.",
        'prevention': "Reduce humidity in greenhouses, space plants properly, prune for better air flow, avoid overhead irrigation."
    },
    'Tomato__Septoria_leaf_spot': {
        'symptoms': "Small, circular spots with dark borders and light gray centers, usually appearing on lower leaves first.",
        'causes': "Fungus Septoria lycopersici, spreads in warm, wet conditions.",
        'solution': "Apply fungicides containing chlorothalonil or copper and remove infected leaves.",
        'prevention': "Use mulch, avoid overhead watering, ensure adequate spacing, practice crop rotation."
    },
    'Tomato__Spider_mites Two-spotted_spider_mite': {
        'symptoms': "Tiny yellow speckling on leaves, fine webbing on undersides of leaves, bronzing of foliage.",
        'causes': "Arachnid Tetranychus urticae, thrives in hot, dry conditions.",
        'solution': "Apply miticides or insecticidal soap, increase humidity around plants.",
        'prevention': "Regularly mist plants to increase humidity, maintain proper irrigation, introduce predatory mites."
    },
    'Tomato__Target_Spot': {
        'symptoms': "Brown to dark brown concentric rings on leaves, stems and fruit.",
        'causes': "Fungus Corynespora cassiicola, favors warm, humid conditions.",
        'solution': "Apply fungicides containing chlorothalonil and ensure good air circulation.",
        'prevention': "Maintain proper plant spacing, avoid overhead irrigation, rotate crops."
    },
    'Tomato__Tomato_Yellow_Leaf_Curl_Virus': {
        'symptoms': "Leaves curl upward and inward, yellowing along leaf margins, stunted growth, flower drop.",
        'causes': "Tomato yellow leaf curl virus (TYLCV) transmitted by whiteflies.",
        'solution': "No cure; remove and destroy infected plants, control whitefly populations.",
        'prevention': "Use virus-resistant varieties, use reflective mulches to repel whiteflies, install insect screening."
    },
    'Tomato__Tomato_mosaic_virus': {
        'symptoms': "Mottled light and dark green on leaves, leaves may be curled or distorted, yellow streaking on fruit.",
        'causes': "Tobacco mosaic virus or tomato mosaic virus, highly contagious through handling and tools.",
        'solution': "No cure; remove and destroy infected plants to prevent spread.",
        'prevention': "Use virus-resistant varieties, wash hands and disinfect tools, don't smoke near plants (tobacco can carry the virus)."
    },
    'Tomato__healthy': {
        'symptoms': "No symptoms of disease, vibrant green leaves, healthy fruit development.",
        'causes': "N/A",
        'solution': "Maintain proper watering and fertilization schedules.",
        'prevention': "Regular pruning, proper spacing, consistent watering, balanced fertilization, crop rotation."
    }
}

# Create a CSV file with headers and data
with open('plant_diseases_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['disease', 'symptoms', 'causes', 'solution', 'prevention']  # Changed from 'disease_name' to 'disease'
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for disease, info in disease_info.items():
        writer.writerow({
            'disease': disease,  # Changed from 'disease_name' to 'disease'
            'symptoms': info['symptoms'],
            'causes': info['causes'],
            'solution': info['solution'],
            'prevention': info['prevention']
        })

print("CSV file 'plant_diseases_info.csv' created successfully!")