class CreateGrantDescriptions < ActiveRecord::Migration[5.2]
  def change
    create_table :grant_descriptions do |t|
      t.text :description
      t.text :term_vector

      t.timestamps
    end
  end
end
