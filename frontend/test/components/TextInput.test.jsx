import { render, screen, fireEvent } from '@testing-library/react'
import TextInput from '../../src/components/TextInput'

describe('TextInput', () => {
  it('renders with initial value and placeholder', () => {
    render(<TextInput text="" setText={() => {}} disabled={false} />)
    const textarea = screen.getByPlaceholderText(/ou cole o conteúdo do email/i)
    expect(textarea).toBeInTheDocument()
    expect(textarea).toHaveValue("")
  })

  it('calls setText on user input', () => {
    const setText = vi.fn()
    render(<TextInput text="" setText={setText} disabled={false} />)
    const textarea = screen.getByPlaceholderText(/ou cole o conteúdo do email/i)

    fireEvent.change(textarea, { target: { value: "Novo texto" } })
    expect(setText).toHaveBeenCalledWith("Novo texto")
  })

  it('is disabled when prop is set', () => {
    render(<TextInput text="" setText={() => {}} disabled={true} />)
    const textarea = screen.getByPlaceholderText(/ou cole o conteúdo do email/i)
    expect(textarea).toBeDisabled()
  })
})
