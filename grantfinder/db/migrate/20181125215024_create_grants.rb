class CreateGrants < ActiveRecord::Migration[5.2]
  def change
    create_table :grants do |t|
      t.string :title
      t.date :release_date
      t.date :expired_date
      t.string :document_number
      t.string :document_type
      t.string :activity_code
      t.string :clinical_trails
      t.string :url

      t.timestamps
    end
  end
end
