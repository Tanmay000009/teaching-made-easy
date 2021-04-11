from flask import Flask,request, url_for, redirect, render_template
from transformers import BertForQuestionAnswering, AutoTokenizer

modelname = 'deepset/bert-base-cased-squad2'

model = BertForQuestionAnswering.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)
from transformers import pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)


app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/redirect')
def redirect():
    return render_template("redirect.html")

@app.route('/checker',methods=['POST','GET'])
def checker():
    if request.method == 'POST':
        Expected_Answer = request.form['Expected_Answer']
        Students_Answer = request.form['Students_Answer']
        print(Expected_Answer)
        print(Students_Answer)
        return render_template("checker.html",Students_Answer=Students_Answer,Expected_Answer=Expected_Answer)
    return  render_template("checker.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        match = request.form["choices-text-preset-values"]
        print(match)
        ref = '''Fibres: All cloth materials are made up of long, narrow, thin structures called fibres. Fibres are obtained from natural as well as man-made sources.
    Natural Sources: Cotton, jute, silk, wool, etc., are obtained from natural sources- plants or animals.
    Man-made Sources: Polyester, nylon, rayon etc., are man-made materials used for making clothes.
    Plant fibres: All the plants have fibres in their body structure, e.g., cotton and mango have fibres on their seed, coconut on its fruit, jute in its stem and banana tree in its leaf.
    Animal fibres: Important animal fibres are wool (hair of sheep) and silk (from silkworm).
    Cotton is the most important industrial crop.
    India was the proud inventor of cotton clothing.
    Cotton has been used in India since 1800 B.C.
    Production: Cotton is grown in Maharashtra, Gujarat, Punjab, Rajasthan, Tamil Nadu and Madhya Pradesh.
    Climate required: Cotton plants need warm climate.
    Cotton is planted early in the spring.
    Black soil is excellent for cotton’s cultivation.
    Cotton bolls: Fruits of cotton plant are spherical-shaped structures of the size of wall nut which are called cotton bolls.
    On maturation, cotton bolls burst open, exposing the white fibres. ‘
    When fibres dry in the sun light, they become fluffy.
    Cotton fibres: Cotton fibres are obtained from cotton bolls.
    Ginning: The process in which seeds from cotton are pulled out by steel combs is called ginning.
    7
    Charkha: Charkha is a machine on which yarn was spun directly from ginned cotton in olden days.
    Bales: Ginned cotton is compressed tightly into bundles weighing approximately 200 kg called bales.
    Sliver: Raw cotton from bales is cleaned, combed and straightened and finally converted into rope like strands called sliver. A sliver of cotton is a loose strand or rope of cotton fibres.
    Yarn: Sliver is pulled and twisted so that the fibre forms a strong thread or yarn.
    
    Twisting of fibres into yarn increases the cohesion and strength of fibres. Handlooms and powerlooms: In villages, the clothes from cotton are woven on small scale known as handlooms. On large scale, cotton clothes are made by machines known as powerlooms.
    Uses of cotton: Cotton is used:
    in manufacturing of textiles.
    as an absorbent in hospital.
    as fillers in mattresses, pillows and quilts.
    as a main raw material for the manufacturing of rayon and paper industry.
    Clothes from cotton are extensively used as mops in household and for cleaning machines in industries.
    Jute is the most extensively used fibre next to cotton.
    It is obtained from the stem of a plant called ‘putson’.
    
    In India, jute is mainly grown in West Bengal, Bihar and Assam.
    Extraction of fibres:
    Jute plants are cut at the time of flowering stage.
    The cut plants are grouped at different places in the fields for few days when most of the leaves dry up and fall down.
    Plants are tied into small bundles.
    Retting: The bundles are made to sink in stagnant water of pond for few days when the gummy skin rots out to separate fibres. The process is called ‘retting’.
    Fibre is extracted from retted jute by hand, with jerks and pulls.
    Uses of jute:
    Jute is extensively used for making gunny bags, potato sacks, carpets, curtains, coarse clothes, ropes, etc.
    These days, fine quality of jute is also used for making jute fabrics. Primitive men and women had no idea about clothes.
    Primitive life was confined mostly to the tropics where the climate was warm and no clothing was needed.
    People migrated to colder regions only after the invention of fire.
    During stone age, people wore bark, big leaves or animal skins.
    People started wearing stitched clothes after the invention of needle about 40,000 to 50,000 years ago.
    Cloth making was developed in three stages:
    First stage was making cloth from plant fibres,
    Second stage began with the use of animal fibres, and
    Third stage began with the development of man-made or synthetic fibres.
    Type of clothings which we wear is influenced by climate, occupation, culture and daily needs.
    Clothing is necessary for the following reasons:
    It protects us from wind and weather.
    It protects us from injury.
    It maintains the body heat.
    Woollen and cotton clothes feel rough and that of rayon, nylon or polyester are smooth to touch.
    Roughness of cotton and woollen fibres is due to the presence of many folds and uneven surface in it.
    Silk, rayon, nylon and polyester are smooth because they have long plain, fine structures.
    Cloth is made from threads and threads, in turn, are spun from fibres.
    All fibres are not suitable for making cloth. Coconut fibres, for instance, are very hard and can only be used for making ropes or as a coir in mattresses.
    Soft and long fibres like cotton, wool, nylon, etc., are suitable to make yam.
    It is advised to wear cotton clothes while working in the kitchen and near fire.
    Cotton wool: The lumps of cotton fibres are called cotton wool. It can be used as absorbent, filling quilts, pillows, etc., and making yam.
    Fabric: Yam can be woven or knitted manually or by machines into fabric.
    Knitting: The process of making fabric from a single yam.
    Spinning: The process of making yam from fibres.
    Weaving: The process of arranging two sets of yam together to make a cloth is called weaving.
    Cotton wool: Cotton wool is obtained from cotton plant. It is made up of thin cotton fibres.
    Fabric: Woven material (cloth) is called fabric.
    Fibre: Thread like animal or plant tissue is called a fibre.
    Knitting: Knitting is a process of making a piece of fabric from a single yam.
    Spinning: The process of making yam from fibres is called spinning.
    Weaving: The process of arranging two sets of yam together to make a fabric is called weaving.
    Yarn: Spun fibres are called yarns.
    Clothes are made of different materials. We get these materials from both plants and animals.
    
    Identify the materials given below as plants or animal product. Write P for the plant products and A for animal products.
    Let us learn about how the story of clothing started, the different materials used to make clothes, and how they are made. Answers: Cotton socks, jute rope, silk cloth, lather shoes.
    History Of Clothing:
    About 30,000 years ago, people started using animal skins for clothing. It is believed that wool was used as early as 6000 years ago.
    Domestication of silkworms to produce silk occurred around 3000 BC in China. In India, cotton came into widespread use around 3000 BC. These fabrics were not stitched. They were just wrapped around the body. Even today, sari, dhoti, and turban are unstitched pieces of cloth.
    
    Fiber And Fabric:
    Clothes are made mostly from fibres. Fibres are thin strands of thread, that are woven to make fabric, for example, cotton fabric, silk fabric, etc. The fabric is stitched to make clothes. For example, cotton fabric can be stitched into a cotton frock or a cotton kurta. There are two main processes of making fabric from fibre – weaving and knitting.
    Weaving: Weaving involves making fabric by arranging two sets of yarn. It is done using a machine called loom, which can be hand-operated (Fig. 4.1) or power- operated. The pattern in which two sets of threads are arranged in a piece of woven cloth is called a weave (Fig. 4.2).
    Knitting: Knitting involves making fabric by forming a series of connected loops of yarn by using knitting needles or machines. Sweaters are made from wool strands by knitting.
    
    Natural And Synthetic Fibres: (Different Types of Fibres)
    Fibres used to make fabric may be natural or synthetic. Fibres that are obtained from plants or animals are called natural fibres. Examples are cotton, jute, wool, and silk. Fibres that are made by man from chemical substances are called synthetic fibres. Examples are nylon, rayon, polyester, and acrylic. Let us learn more about plant fibres.
    Plant Fibres:
    Cotton (Fig. 4.3), jute, coir, silk cotton, hemp, and flax are examples of plant fibres. Denim, used to make jeans, is made from cotton.
    
    Cotton:
    The cotton plant is a shrub. It grows well in black soil and warm climate. It needs moderate rainfall. Cotton is a soft fibre that grows around the seeds of the cotton plant. A variety of textile products are made from cotton. In India, ‘lchadi’, a coarse hand-woven cloth, is made from cotton.
    
    
    Jute:
    Jute is a fibre obtained from the bark of the jute plant (Fig. 4.6). It can be grown in different soil types, ranging from clayey to sandy soil. It grows best in loamy soil (mixture of sand, silt, and clay), sandy soil, and clayey soil. It grows well in regions where it rains a lot. Almost 80% of the world’s high-quality jute comes from Bangladesh. Bangladesh, India, China, Nepal, and Thailand are the main producers of jute.
    
    Other Useful Plant Fibres:
    There are other important plant fibres as well.
    Coir: Coir is the fibre obtained from the outer covering or the husk of the coconut. Usually coconuts are left in water for a few months. The husk is then separated from the nut and beaten with wooden mallets to get the fibre. The fibre thus obtained is spun and dyed and is ready for weaving. Coir is used to make several household products like rope and floor covering and also as a stuffing in mattresses and pillows.
    
    Silk cotton: Silk cotton is another plant fibre that is commonly used as a stuffing in pillow, sleeping bag, and life jacket. This fibre is obtained from the silk cotton tree, also called kapok.
    The fruits of the kapok tree contain fibres that are light and fluffy (like cotton). When the fruit ripens, it bursts open, releasing the fibres.
    Hemp: Hemp fibres are obtained from the stem of the hemp plant. Hemp fibres are used in the production of ropes, carpets, nets, clothes, and paper.
    Flax Fibres obtained from the stem of the flax plant are woven to make a fabric called linen. Flax fibres are also used in the production of rope and high-quality paper.
    Fabric The material made by weaving the threads from fibres is called fabric.
    Weaving Weaving involves the making of fabric from yarn.
    Ginning The process of separating the cotton fibres from its seeds is called ginning.
    Spinning The process of making yarn from fibres is called spinning.
    Retting The process of rotting the stems of the plants in water to remove the sticky substance and separate fibres is called retting.
    Clothing materials are obtained from both plants and animals.
    Fibres are woven to make fabrics and fabrics are stitched to make clothes.
    Fibres may be natural or synthetic.
    Cotton, jute, coir, silk cotton, hemp, and flax are some plant fibres.'''
        ans = nlp({
            'question': match,
            'context': ref
        })
        start = ref[:ans["start"]]
        high = ref[ans["start"]:ans["end"]]
        end = ref[ans["end"]:]
        print(ans)
        score = ans["answer"]
        return render_template('index.html',start=start ,high=high, end=end)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
