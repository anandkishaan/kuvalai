from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'kuvalai-secret'

# --- Config ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kuvalai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
db = SQLAlchemy(app)

# --- Models ---
class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(50))
    name_ta = db.Column(db.String(50))
    image = db.Column(db.String(100))

class Chemical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(50))
    name_ta = db.Column(db.String(50))
    image = db.Column(db.String(100))

class Sprayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(50))
    name_ta = db.Column(db.String(50))
    image = db.Column(db.String(100))

class DosageGuide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chemical_id = db.Column(db.Integer, db.ForeignKey('chemical.id'))
    sprayer_id = db.Column(db.Integer, db.ForeignKey('sprayer.id'))
    image = db.Column(db.String(100))
    guide_en = db.Column(db.String(200))
    guide_ta = db.Column(db.String(200))

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    crops = Crop.query.all()
    if request.method == 'POST':
        selected_crop = request.form['crop']
        return render_template('chemical.html', crop=selected_crop, chemicals=Chemical.query.all())
    return render_template('crop.html', crops=crops)

@app.route('/chemical', methods=['POST'])
def chemical():
    crop = request.form['crop']
    chemical = request.form['chemical']
    return render_template('sprayer.html', crop=crop, chemical=chemical, sprayers=Sprayer.query.all())

@app.route('/sprayer', methods=['POST'])
def sprayer():
    crop = request.form['crop']
    chemical = request.form['chemical']
    sprayer = request.form['sprayer']
    chem_obj = Chemical.query.filter_by(name_en=chemical).first()
    sprayer_obj = Sprayer.query.filter_by(name_en=sprayer).first()

    if not chem_obj or not sprayer_obj:
        return "Error: Data not found", 400

    guide = DosageGuide.query.filter_by(chemical_id=chem_obj.id, sprayer_id=sprayer_obj.id).first()
    return render_template('result.html',
                           crop=crop,
                           chemical=chemical,
                           sprayer=sprayer,
                           image=guide.image if guide else "default.png",
                           guide_en=guide.guide_en if guide else "No guideline found.",
                           guide_ta=guide.guide_ta if guide else "வழிகாட்டல் இல்லை.")

# --- Admin Panel ---
@app.route('/admin')
def admin_page():
    return render_template('admin.html',
                           crops=Crop.query.all(),
                           chemicals=Chemical.query.all(),
                           sprayers=Sprayer.query.all(),
                           guides=DosageGuide.query.all())

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect('/admin')

@app.route('/add_crop', methods=['POST'])
def add_crop():
    db.session.add(Crop(name_en=request.form['name_en'], name_ta=request.form['name_ta'], image=request.form['image']))
    db.session.commit()
    return redirect('/admin')

@app.route('/add_chemical', methods=['POST'])
def add_chemical():
    db.session.add(Chemical(name_en=request.form['name_en'], name_ta=request.form['name_ta'], image=request.form['image']))
    db.session.commit()
    return redirect('/admin')

@app.route('/add_sprayer', methods=['POST'])
def add_sprayer():
    db.session.add(Sprayer(name_en=request.form['name_en'], name_ta=request.form['name_ta'], image=request.form['image']))
    db.session.commit()
    return redirect('/admin')

@app.route('/add_guide', methods=['POST'])
def add_guide():
    db.session.add(DosageGuide(
        chemical_id=request.form['chemical_id'],
        sprayer_id=request.form['sprayer_id'],
        image=request.form['image'],
        guide_en=request.form['guide_en'],
        guide_ta=request.form['guide_ta']
    ))
    db.session.commit()
    return redirect('/admin')

@app.route('/delete/<model>/<int:id>', methods=['POST'])
def delete_item(model, id):
    model_map = {'crop': Crop, 'chemical': Chemical, 'sprayer': Sprayer, 'guide': DosageGuide}
    obj = model_map.get(model).query.get(id)
    if obj:
        db.session.delete(obj)
        db.session.commit()
    return redirect('/admin')

# --- Init DB ---
if __name__ == '__main__':
    if not os.path.exists('kuvalai.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
