// import methods from "./CHANNELS/index.js";
import { default as knex } from './index.js'

const mapArray = (list, cols) => {
  const array = []
  for (const row of list) {
    array.push(map(row, cols))
  }
  return array
}

const map = (conditions, cols) => {
  const mapped = {}
  for (const key of Object.keys(cols)) {
    mapped[cols[key]] = conditions[key]
  }
  return mapped
}

export const select = async (table, conditions) => {
  const { name, columns } = table
  const mapped = map(conditions, columns)
  return knex(name).select(columns).where(mapped)

}
export const insert = async (table, vals) => {
  const { name, columns } = table
  let mapped
  if (Array.isArray(vals))
    mapped = mapArray(vals, columns)
  else mapped = map(vals, columns)
  return knex(name).insert(mapped).onConflict().ignore()
}
