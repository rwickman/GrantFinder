# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2018_11_25_215434) do

  create_table "grant_descriptions", force: :cascade do |t|
    t.text "description"
    t.text "term_vector"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "grant_id"
    t.index ["grant_id"], name: "index_grant_descriptions_on_grant_id"
  end

  create_table "grants", force: :cascade do |t|
    t.string "title"
    t.date "release_date"
    t.date "expired_date"
    t.string "document_number"
    t.string "document_type"
    t.string "activity_code"
    t.string "clinical_trails"
    t.string "url"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
